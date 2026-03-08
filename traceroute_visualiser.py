import subprocess
import re
import geoip2.database
import folium

import os
import webbrowser

ROUTE_COLORS = ["red", "blue", "green", "purple", "orange","darkred", "cadetblue", "darkgreen", "black"]

def read_destinations(destination_list):
    destinations=[]

    with open(destination_list,'r') as file:
        for line in file:
            line=line.strip()
            if line:
                destinations.append(line)

    return destinations

def run_traceroute(destination):
    result=subprocess.run (
        ["traceroute", destination],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout

def extract_ips(traceroute_output):
    ip_pattern=r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    ips=re.findall(ip_pattern,traceroute_output)
    unique_ips=[]

    for ip in ips:
        if ip not in unique_ips:
            unique_ips.append(ip)

    return unique_ips

def geolocate_ips(ips):
    reader=geoip2.database.Reader("GeoLite2-City.mmdb")

    geo_info=[]
    for ip in ips:
        try:
            response=reader.city(ip)

            geo_info.append({
                "ip":ip,
                "latitude":response.location.latitude,
                "longitude":response.location.longitude
            })
        except:
            geo_info.append({
                "ip":ip,
                "latitude":None,
                "longitude":None
            })
    reader.close()
    return geo_info

def visualise(m,geo_data,destination,color):
    valid_hops=[
        hop for hop in geo_data
        if hop["latitude"] is not None and hop["longitude"] is not None
    ]
    if not valid_hops:
        return 

    points=[]

    for hop in valid_hops:
        lat=hop["latitude"]
        lon=hop["longitude"]

        points.append((lat,lon))

        popup_text = f"""
        Destination: {destination}<br>
        IP: {hop['ip']}
        """

        folium.Marker(
            location=[lat,lon],
            popup=popup_text,
            icon=folium.Icon(color="blue",icon="info-sign")
        ).add_to(m)

    folium.PolyLine(points,color=color,weight=3,tooltip=destination).add_to(m)
    

if __name__ == "__main__":
    destinations=read_destinations("destination_list.txt")
    ROUTE_COLORS = ["red", "blue", "green", "purple", "orange","darkred", "cadetblue", "darkgreen", "black"]

    m = folium.Map(location=[20, 0], zoom_start=2)
    for i, destination in enumerate(destinations):
        print(f"\nRunning traceroute to: {destination}\n")

        output = run_traceroute(destination)
        ips = extract_ips(output)
        geo_data = geolocate_ips(ips)

        color = ROUTE_COLORS[i % len(ROUTE_COLORS)]
        visualise(m,geo_data, destination, color)

    output_file = "traceroute_all_destinations.html"
    m.save(output_file)

    full_path = os.path.abspath(output_file)
    webbrowser.open(f"file://{full_path}")

    print(f"\nAll traceroute paths saved in: {output_file}")



 

