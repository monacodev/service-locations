import folium
from geopy.geocoders import Nominatim 

def geolocalise_me(location):

    """
     return : longitude and latitude

    """
    # on récup le nom du Lieux 
    loc = Nominatim(user_agent="GetLoc") 

    # le tooltip du marker est le mesage de la bulle quand on fait un hover du marker et il est sous format string  en global comme ça il s'applique pour tous les markers 
    tooltip = "infos"

    # prend le nom du lieux dont on veut récupérer les coordonées lat et long
    Location = loc.geocode(location)

    # récupérer de lat et long
    print(Location.latitude)

    # récupérer de lat et long
    print(Location.longitude)

    map_object =  folium.Map(location = [Location.latitude, Location.longitude], zoom_start = 14)

    # ajout du marker à la carte map 
    folium.Marker([Location.latitude, Location.longitude] , popup='<strong>Location one</strong>', tooltip=tooltip).add_to(map_object)

    # création de la carte map dans un fichier html
    map_object.save('index.html')

    return Location

print(geolocalise_me("Bourg, Lille"))

