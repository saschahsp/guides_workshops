# Our First Map - Top 10 Pickup Stations

## About Displaying Maps in Zeppelin

This example will plot our top bike pickup/dropoff stations on a map. To do so,

* We'll use Spark code to gather the data that we will use to define specific markers to add to our map. We will bind this marker data to a named angular variable. Angular is the framework that Zeppelin uses for its UI. here
* Then we will create a %angular paragraph to hold some custom HTML/javascript code. This is the paragraph that will display the map. Our code will use the javascript Leaflet project (here) to create an html/javascript map object. As part of our javascript, we'll instruct it to listen for changes to our named angular variable that we are populating in our spark paragraph. When the angular variable changes, our code will re-draw the markers on the map.

This approach is derived from examples on the internet, such as here or here, that are all based on a similar approach.

## Our First Map - Top 10 Pickup Stations

To get started, we will plot the 10 top pickup stations on a map. We will have 1 paragraph which will use Spark and Spark SQL to query our bike_trips table and save the results into an angular variable. And we will have 1 paragraph that contains the html/javascript to display our map.

* Run the “Spark code for our first map” to gather the data for our map
* Then run the “HTML/Javascript for our first map” to display the map with the selected data

```scala
%spark


//a previous tutorial placed the csv file into your Object Store citibike container
//notice the use of the swift://CONTAINER.default/ syntax
val Container = "bigdataprep"
val Directory = "citibike"

var df: org.apache.spark.sql.DataFrame = null

println("Running on OCI");
df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").load("oci://bigdataprep@sehubpilot/"+Directory+"/raw/201612-citibike-tripdata.csv")



// If you get this error message:
// java.lang.IllegalStateException: Cannot call methods on a stopped SparkContext.
// Then go to the Settings tab, then click on Notebook.  Then restart the Notebook.  This will restart your SparkContext


df.createOrReplaceTempView("bike_trips_temp")

//Define a class for the structure of the data we will be passing to the map javascript code
case class Stations(ridetype: String, station: String, trips: String, lat: Double, lon: Double)

//Unbind angular variable in case it already exists from previous run
z.angularUnbind("topstations") 

//Define a new dataframe based off a query
val topstationsDF = sqlContext.sql(s"""select "Start" ridetype, `Start Station Name` station,`Start Station Latitude` lat,`Start Station Longitude` lon, count(*) trips from bike_trips_temp 
group by `Start Station Name`,`Start Station Latitude`,`Start Station Longitude`
order by count(*) desc limit 10""")


//Map the DF into an Array of Stations
var items = topstationsDF.map(b => Stations(b(0).toString, b(1).toString, "Pickups:"+b(4).toString, b(2).toString.toDouble, b(3).toString.toDouble)).collect

//Bind the TopStations (as an Array) to an Angular variable named topstations
z.angularBind("topstations", items) 

println("..")
println("done")
```

```java
%angular
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.css" />
<div id="firstmap" style="height: 600px; width: 100%"></div>

<script type="text/javascript">

//based on https://gist.github.com/granturing/a09aed4a302a7367be92, https://community.hortonworks.com/articles/90320/add-leaflet-map-to-zeppelin-notebook.html, etc

function initMap() {
    //open up a map around NYC at zoom level 13
    var map = L.map('firstmap', {preferCanvas: true}).setView([40.75, -73.99], 13);

    //define the background tile layer using OpenStreet maps.  Leaflet can work with other providers, too
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 16,
        minZoom: 11
    }).addTo(map);

    var geoMarkers = L.layerGroup().addTo(map);
    
    // setup a custom icon for markers. See https://github.com/pointhi/leaflet-color-markers
    var greenIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });
    
    var redIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });

    var el = angular.element($('#firstmap').parent('.ng-scope'));
    angular.element(el).ready(function() {
        
        //listen for changes to the angular variable called stations
        window.locationWatcher = el.scope().compiledScope.$watch('topstations', function(newValue, oldValue) {

            //loop through each entry in our stations variable and add it as a marker
            angular.forEach(newValue, function(station) {
                var marker = L.marker([station.lat, station.lon])
                marker.addTo(geoMarkers);  

            });
        })
    });
}

if (window.locationWatcher) {
    // clear existing watcher otherwise we'll have duplicates
    window.locationWatcher();
}

// ensure we only load the script once, seems to cause issues otherwise
if (window.L) {
    initMap();
} else {
    console.log('Loading Leaflet library');
    var sc = document.createElement('script');
    sc.type = 'text/javascript';
    sc.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.js';
    sc.onload = initMap;
    sc.onerror = function(err) { alert(err); }
    document.getElementsByTagName('head')[0].appendChild(sc);
}
</script>
```

## A more complex example - Top Pickup and Dropoff locations for certain times of day

Now that we have shown a simple example of a map, we will show a more complex example using a parameter-driven query with multiple map markers and layers.

To run this example:

Use the Query Parameters paragraph to choose the time frame for the query as well as how many of the Top pickup and dropoff stations to show on the map.

Then run the Query Parameters paragraph. This will query the desired data (by automatically running the “Spark code for the more complex map” paragraph)

Once the data has been queried (takes about 20 seconds), the “More Complex Map” will be updated. If the map is not showing, then play the “More Complex Map” paragraph to make it visible.
- Pickups are drawn in green. Dropoffs are in red.
- Use the layers control in the upper right of the map to show/hide pickup and dropoff stations.
- The size of the circle on the map represents the number of pickups/dropoffs for that station during the selected time frame.

```scala
%spark
z.angularBind("BIND_topN", z.select("Top N","10",Seq(("5","5"),("10","10"),("20","20"),("50","50"),("100","100"))))
z.angularBind("BIND_dayOfWeek", z.select("dayOfWeek", "All", Seq(("All", "All"),
                         ("MonFri", "Mon-Fri"), ("SatSun","Weekend")))  )
z.angularBind("BIND_hourOfDay", z.select("hourOfDay", "All", Seq(("All", "All"),
                         ("Morning", "7am to 10am"), ("Midday","11am to 3pm"),("Afternoon","4pm to 7pm"),
                         ("Evening","8pm to 11pm"),("LateNite","12am to 6am")))  )
                         
z.run("20190826-134402_1561120541")                      
						 
```

```scala
%spark

//Define a class for the structure of the data we will be passing to the map javascript code
case class Stations(ridetype: String, station: String, trips: String, lat: Double, lon: Double, radius: Double)

z.angularUnbind("stations")

{
//Be sure to have run Part 1 prior to running this as this assumes that the bike_trips table is part of your current session

//Define some UI widgets for data selection parameters
// Learn more here: https://zeppelin.apache.org/docs/0.6.1/interpreter/spark.html#form-creation


//Use our UI values to define custom SQL
var limitString = " limit "+z.angular("BIND_topN")
var whereString = " where 1=1 "

if (z.angular("BIND_dayOfWeek")=="MonFri") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"E") in ("Mon","Tue","Wed","Thu","Fri") """
} else if (z.angular("BIND_dayOfWeek")=="SatSun") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"E") in ("Sat","Sun") """
}

if (z.angular("BIND_hourOfDay")=="Morning") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("7","8","9","10") """
} else if (z.angular("BIND_hourOfDay")=="Midday") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("11","12","13","14","15") """
} else if (z.angular("BIND_hourOfDay")=="Afternoon") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("16","17","18","19") """
} else if (z.angular("BIND_hourOfDay")=="Evening") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("20","21","22","23") """
} else if (z.angular("BIND_hourOfDay")=="LateNite") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("0","1","2","3","4","5","6") """
}

println("WHERE STRING: "+whereString)

//Define a new dataframe based off a query
var stations = sqlContext.sql(s"""select "Start" ridetype, `Start Station Name` station,`Start Station Latitude` lat,`Start Station Longitude` lon, count(*) trips from bike_trips_temp """ +
whereString + s"""
group by `Start Station Name`,`Start Station Latitude`,`Start Station Longitude`
order by count(*) desc """ + limitString)


//Map the DF into an Array of Stations
var items1 = stations.map(b => Stations(b(0).toString, b(1).toString, "Pickups:"+b(4).toString, b(2).toString.toDouble, b(3).toString.toDouble,  b(4).toString.toDouble/8 )).collect



//now do the same for top ending stations
stations = sqlContext.sql(s"""select "End" ridetype, `End Station Name` station,`End Station Latitude` lat,`End Station Longitude` lon, count(*) trips from bike_trips_temp """ +
whereString + s"""
group by `End Station Name`,`End Station Latitude`,`End Station Longitude`
order by count(*) desc """ + limitString)
	
//Map the DF into an Array of Stations.  Offset the lat,lon by a bit so you see both Start and End markers
var items2 = stations.map(b => Stations(b(0).toString, b(1).toString, "Dropoffs:"+b(4).toString, b(2).toString.toDouble+0.0001, b(3).toString.toDouble+0.0001, b(4).toString.toDouble/8)).collect

//combine the two arrays
val combined=items1 ++ items2

//Bind the Stations to an Angular variable named stations
z.angularBind("stations", combined) 

println("done")
}
```

```java
%angular
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.css" />
<div id="map" style="height: 600px; width: 100%"></div>

<script type="text/javascript">

//based on https://gist.github.com/granturing/a09aed4a302a7367be92, https://community.hortonworks.com/articles/90320/add-leaflet-map-to-zeppelin-notebook.html, etc

function initMap() {
    //open up a map around NYC at zoom level 13
    var map = L.map('map', {preferCanvas: true}).setView([40.75, -73.99], 13);

    //define the background tile layer using OpenStreet maps.  Leaflet can work with other providers, too
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 16,
        minZoom: 11
    }).addTo(map);

    //define a new LayerGroup which will hold our markers
    var startMarkers = L.layerGroup().addTo(map);
    var endMarkers = L.layerGroup().addTo(map);

    var overlayMaps = {
    "Top Pickup Stations": startMarkers,
    "Top Dropoff Stations": endMarkers
    };
    
    //add a Control to the map to let the user click the Marker layer off and on
    L.control.layers(null, overlayMaps).addTo(map);
    
    // keep track of our markers, so we can remove them later
    var markers = new Array();
    
    // setup a custom icon for markers. See https://github.com/pointhi/leaflet-color-markers
    var greenIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });
    
    var redIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });

    var el = angular.element($('#map').parent('.ng-scope'));
    angular.element(el).ready(function() {
        
        //listen for changes to the angular variable called stations
        window.locationWatcher = el.scope().compiledScope.$watch('stations', function(newValue, oldValue) {
             //startMarkers.clearLayers(); -- this did not work for me, so I use the for loop below to delete old markers
            for(i=0;i<markers.length;i++) {
               startMarkers.removeLayer(markers[i]);
               endMarkers.removeLayer(markers[i]);
               map.removeLayer(markers[i]);
            }  
            //now empty our array and start again
            markers = new Array();
            
            //loop through each entry in our stations variable and add it as a marker
            angular.forEach(newValue, function(bikes) {
                var marker = L.marker([bikes.lat, bikes.lon], {icon: greenIcon})
                    .bindPopup("<b>" + bikes.station + "</b><br>" + bikes.trips)
                var circle = L.circle([bikes.lat, bikes.lon], bikes.radius,{
                       color: 'green',
                       fillColor: '#5f0',
                       fillOpacity: 0.5 })
                   
                if (bikes.ridetype=="End") {
                    marker.setIcon(redIcon)
                    marker.addTo(endMarkers)
                    circle.setStyle({
                       color: 'red',
                       fillColor: '#f03',
                       fillOpacity: 0.5 })
                    circle.addTo(endMarkers)
                } else {
                    marker.addTo(startMarkers);  
                    circle.addTo(startMarkers);  
                }
                markers.push(circle);   
                markers.push(marker);   

            });
        })
    });
}

if (window.locationWatcher) {
    // clear existing watcher otherwise we'll have duplicates
    window.locationWatcher();
}

// ensure we only load the script once, seems to cause issues otherwise
if (window.L) {
    initMap();
} else {
    console.log('Loading Leaflet library');
    var sc = document.createElement('script');
    sc.type = 'text/javascript';
    sc.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.js';
    sc.onload = initMap;
    sc.onerror = function(err) { alert(err); }
    document.getElementsByTagName('head')[0].appendChild(sc);
}
</script>
```

