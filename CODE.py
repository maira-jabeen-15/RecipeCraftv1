
print("What do you crave right now?")
print("Brownies[D01]" , "Chocolate Chip Cookies[D02]", "Gulab Jamun[D03]", "Chicken Biryani[M01]", sep ="\n" )
food = input("Type the recipe code and lets get cookin'!! ")

recipes = {"D01": "brownies.txt", "D02": "chocolate_chip_cookies.txt", "D03" : "gulab_jamun.txt", "M01" : "chicken_biryani.txt" } #make this later, checks for which recipe the user wants
servings = int(input("How many people are you cooking for? "))    #MAKE A VARIABLE THAT GETS THE VALUE FROM THE DICT AND PASSESS IT TO WITH OPEN

############################# EXTRACTING INGREDIENTS FROM TEXT FILE###########
flag = False
with open(recipes[food],"r") as file:
        ingredients=[]
        for line in file:
            l = line.strip()     #this line being accessed is a string 
            # print(line.strip())  #using .strip() to remove extra spaces 
            
            if "----------" in line:
                  flag = False

            if flag == True:
                  
                  x=line.split()
                  ingredients.append(x)
                  
            if "Ingredients:" in line:
                  flag = True
                
       
        #SINCE EVERYTHING IN A TEXT FILE IS TYPE STR, THIS CODE CHECKS IF THE FIRST ELEMENT OF THE
        # LIST OF NESTED LIST IS AN INTEGER AND THEN CONVERTS THE ENTIRE ELEMENT TO INT


        for i in range(len(ingredients)) :
              for j in range(len(ingredients[i])):
                    if ingredients[i][j][0] in "0123456789":  #IF I DIDNT PUT[0] HERE, IT ONLY CONVERTS ONE DIGIT MEASUREMENT TO INTEGER
                          ingredients[i][j] = int(ingredients[i][j])        

        def multiplier(ingredients, servings):
            if servings == 1:
                  return ingredients
            elif servings > 1:
                  for i in range(len(ingredients)):
                        for j in range(len(ingredients[i])):
                              if type(ingredients[i][j]) == int:
                                    ingredients[i][j] = servings * ingredients[i][j]
                  return ingredients
            
        
        (multiplier(ingredients, servings))
            
# -------------------- DIETARY RESTRICTIONS & SUBSTITUTIOS --------------------

dietary_keywords = {
    "lactose intolerance": ["milk", "butter", "cream", "cheese", "yogurt", "yoghurt"],
    "peanut allergy": ["peanut", "groundnut"],
    "gluten allergy": ["flour", "wheat", "bread", "pasta", "barley", "rye", "couscous", "breadcrumbs"]
}

substitutes = {
    "milk": "oat milk or almond milk",
    "butter": "plant-based butter",
    "cream": "coconut cream",
    "cheese": "vegan cheese",
    "yogurt": "coconut yogurt",
    "yoghurt": "coconut yogurt",
    "peanut": "sunflower seed butter",
    "groundnut": "sunflower seeds",
    "flour": "gluten-free flour blend",
    "wheat": "gluten-free flour blend",
    "bread": "gluten-free bread",
    "pasta": "gluten-free pasta",
    "barley": "quinoa",
    "rye": "gluten-free oats",
    "couscous": "quinoa",
    "breadcrumbs": "gluten-free breadcrumbs"
}


print("\nDo you have any dietary restrictions?")
print("1. Lactose intolerance")
print("2. Peanut allergy")
print("3. Gluten allergy")
print("0. No restrictions")

restriction_options = {
    "1": "lactose intolerance",
    "2": "peanut allergy",
    "3": "gluten allergy"
}

selected_restrictions = []

choice = input("Enter your choice (e.g. 1,3): ")

choices = choice.split(",")

for item in choices:
    item = item.strip()
    if item in restriction_options:
        selected_restrictions.append(restriction_options[item])


# Recrsive call to check for restrictions and their subs
def check_substitutions_recursive(ingredients_list, selected_restrictions):
    # BASE CASE: Stop when there are no ingredients left to check
    if len(ingredients_list) == 0:
        return []
    
    #  checks the first ingredient in the list 
    current_ingredient = ingredients_list[0]
    ingredient_name = " ".join(map(str, current_ingredient)).lower()
    current_matches = []
    
    for restriction in selected_restrictions:
        for keyword in dietary_keywords[restriction]:
            if keyword in ingredient_name:
                sub_item = substitutes[keyword]
                current_matches.append([ingredient_name, sub_item])
                break
    
    #  Combine current matches with the recursive check of the remaining ingredients
    return current_matches + check_substitutions_recursive(ingredients_list[1:], selected_restrictions)

suggested_substitutes = check_substitutions_recursive(ingredients, selected_restrictions)


# Outputting the result
print("\nDietary Restriction Results:")

if len(suggested_substitutes) == 0:
    print("No matching ingredients found. Safe to cook!")
else:
    print("The following ingredients need to be substituted:")
    for i in range(len(suggested_substitutes)):
        original_ing = suggested_substitutes[i][0]
        replacement = suggested_substitutes[i][1]
        print("- " + original_ing + " --> Replace with: " + replacement)

loop = True

with open (recipes[food], "r") as recipe:
        for line in recipe:
            if loop == True:
                  if "serving size:" in line:
                        print("serving size:", servings)
                  else:
                        
                        if "Ingredients:" not  in line:
                              print(line)
                        
                        elif "Ingredients:" in line:
                              print(line)
                              loop = False
                              for i in ingredients:
                                    for j in i:
                                          print(j,end=" ")
                                    print()
                        
            elif "Instructions:" in line:
                        loop = True
                        print(line)

        
