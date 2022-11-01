# When you retrieve the value using square brackets

alien_0 = {"color":"green", "speed":"slow"}
print(alien_0['points'])

# get() > to set a default value that will be returned if the requested key doesn't exist

alien_0 = {"color":"green", "speed":"slow"}

point_value = alien_0.get("points","No point value assigned.")
print(point_value)  # clean message instead of an error
