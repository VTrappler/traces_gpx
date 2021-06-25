from gpxplotter import read_gpx_file

for tracks in read_gpx_file('28_nov._14h20_-_15h47.gpx'):
    print(tracks.keys())
