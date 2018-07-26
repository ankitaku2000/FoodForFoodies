import models

# 1=apple Pie
# 2=apple Empanadas
# 3=danish apple Pie
# 4=apple Tart
# 5=apple Slaw

# 6=shrimp Paella
# 7=bacon buffalo shrimp
# 8=croatian shrimp
# 9=shrimp stir fry
# 10=piri shrimp

# 11=Postre Chaja Peach Meringue Cake
# 12=Peach Cobbler
# 13=peach dumpling
# 14=Peach chicken
# 15=peach phrini


def get_recipes_directions ():
    directions_array=["Heat oven to 425F. Prepare Double-Crust Pastry",
    "Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.",
    "Stir in apples. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate",
    "Roll other round of pastry. Fold into fourths and cut slits so steam can escape. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.",
    "Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning.",
    "Remove foil during last 15 minutes of baking",
    "Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired."]

    ingredients_array=["1/3 to 1/2 cup sugar", "1/4 cup Gold Medal all-purpose flour", "1/2 teaspoon ground cinnamon",
    "1/2 teaspoon ground nutmeg", "1/8 teaspoon salt", "8 cups thinly sliced peeled tart apples (8 medium)",
     "2 tablespoons butter or margarine"]

    apple_pie= models.Recipe(name_displayed="All-American Apple Pie", food_name="apple_pie", ingredients=ingredients_array,
    directions=directions_array, picture="/static/applepie.jpeg")

    apple_pie.put()


    ingredients2_array=["2 cups flour", "2 egg yolks beaten", "1 whole egg", "1 tablespoon sugar",
    "1/2 cup Water", "1/2 teaspoon salt",
     "3 large apples",  "1/2 cup brown sugar", "1 tablespoon ground cinnamon",
    "1/4 teaspoon ground nutmeg", "powder sugar to sprinkle"]

    directions2_array=["Crack the 2 eggs and add the water, salt to the eggs, mixing them thoroughly.",
    "pour them into a mixing bowl along with the flour, use hands to knead the dough.",
    "Set aside the dough for 10-12 minutes to set.",
    "Start rolling out the dough on the cutting board as thin as you can about 1/8 inch or less.",
    "Using a round plate or a giant cookie cutter, cut the dough into 4-inch circles.",
    "place about a 2 tablespoons of apple filing in one side of the dough.",
    "place about a 2 tablespoons of apple filing in one side of the dough.",
    "Fold it in half and curl up the edges of the empanada to seal it.",
    "Crack the extra egg and whisk it up with a splash of cold water until pale yellow and perfectly mixed.",
    "Just before the empanadas go in the oven, use a pastry brush and paint them with a light, even coat of egg wash Bake for 8-10 minutes at 350 degrees."
    "In a saucepan cook the apples with the sugar, cinnamon and nutmeg on medium heat. Cook for about 5-7 minutes until apples are soft and translucent.",
    "Let it cool off and sprinkle with powdered sugar"]

    apple_empanadas=models.Recipe(name_displayed="Apple Empanadas", food_name="apple_empanadas", ingredients=ingredients2_array, directions=directions2_array, picture="/static/appleempanadas.png")


    apple_empanadas.put()

    ingredients3_array=["1 cup sugar", "8 ounces butter at room temperature",
    "4 large eggs room temperature", "2 cups all-purpose flour",
    "1 teaspoon baking powder", "1/2 teaspoon salt", "1 teaspoon vanilla extract", "6 apples",  "1/2 cup sugar", "1 tablespoon cinnamon"]

    directions3_array=["Preheat oven to 350F. Line the bottom of a 9-inch springform pan with parchment paper.",
    "Spray the pan with baking spray and rub with a paper towel to evenly coat.",
    "In a small bowl, combine 1/2 cup sugar with 1 tablespoon cinnamon.",
    "Combine flour,baking powder and salt. Stir well.",
    "Peel and core apples, cut into quarters and then cut each quarter into thin slices.",
    "In the bowl of an electric mixer, beat butter and sugar until thick and smooth. Add vanilla then add eggs, one at the time, beating for 30 seconds after each addition.",
    "Stop to scrape down sides of bowl once or twice.",
    "With mixer on low speed, add flour mixture and mix just until combined.",
    "Combine the apples with the cinnamon/sugar mixture. Add half of the apples to the prepared pan.",
    "Pour batter over apples and smooth batter to edges of pan. Starting in the center, add remaining apples in a circular pattern on top of the batter.",
    "Sprinkle any remaining cinnamon/sugar mixture over the top of the apples.",
    "Bake cake for one hour. Cover loosely with foil and bake another 15-20 minutes or until set in the center. Check to see if a toothpick inserted in the center comes out clean.",
    "Cool on a baking rack before removing outer ring. Serve warm or at room temperature with a dollop of whipped cream or ice cream. Enjoy!"]

    danish_apple_pie=models.Recipe(name_displayed="Danish Apple Cake", food_name="danish_apple_pie", ingredients=ingredients3_array, directions=directions3_array, picture="/static/danishapplepie.jpg")

    danish_apple_pie.put()

    ingredients4_array=["1/2 cup mayonnaise", "2 tablespoons apple cider vinegar",
    "1 tablespoon sugar", "1 tablespoon grainy mustard", "1/2 teaspoon salt",
    "1/2 teaspoon celery seed", "1/2 teaspoon black pepper", "4 cups shredded cabbage",
    "2 tart apples (cored, julienned or shredded)", "1 cup carrots shredded"]

    directions4_array=["Combine dressing ingredients in a small bowl & set aside", "Toss with slaw ingredients", "Allow to sit for at least 1 hour before serving"]

    apple_slaw=models.Recipe(name_displayed="Apple Slaw", food_name="apple_slaw", ingredients=ingredients4_array, directions=directions4_array, picture="/static/appleslaw.jpg")

    apple_slaw.put()

    ingredients5_array=["1 cup sugar", "3 tablespoons butter", "3 large eggs", "1 cup self raising flour", "2 ml baking powder", "pinch of salt",
    "1/4 cup (60 ml) milk", "1 small tin (385 g) of tart apples (unsweetened)", "1 Tin Cream", "1 Cup Sugar"]

    directions5_array=["Preheat oven to 180C", "Beat the butter and sugar until light and fluffy.", "Add the eggs one at a time", "Sift the flour, baking powder and salt and add to the mixture.",
    "Mix slightly and add the milk little by little", "Add the batter in prepared baking dish and place the apples on top.",
    "Bake for 30-40 minutes until light brown.", "Heat the Tin Cream in a saucepan with the sugar until sugar is completely dissolved. Pour over warm apple tart."]

    apple_tart=models.Recipe(name_displayed="South African Apple Tart", food_name="apple_tart", ingredients=ingredients5_array, directions=directions5_array, picture="/static/appletart.jpg")

    apple_tart.put()

    ingredients6_array=["1 pound frozen raw shrimp", "3 tablespoons achiote oil orolive oil", "1 large onion, chopped", "4 cloves garlic, chopped", "1 tablespoon aji amarillo chili pepper paste",
    "1 teaspoon cumin", "1 package Sazon Goya with azafron (saffron)", "1 teaspoon salt",
    "2 tomatoes, chopped", "3 cups rice", "1/2 cup white wine", "2 cups frozen green peas (optional)", "Salt and pepper, to taste", "2 tablespoons minced cilantro", "Juice of 1 lime"]

    directions6_array=["Bring a pot of salted water to a boil. Add the shrimp and cook for 2 minutes, until they just turn pink.", "Remove the shrimp from the water with a slotted spoon and place shrimp in a bowl of ice water.", "Put the oil in a skillet over medium heat.",
    "Add the chopped onion and garlic and cook until translucent and fragrant.", "Add the aji amarillo paste, cumin, Sazon Goya, salt and tomatoes to the onions and garlic.", "Continue cooking for several minutes more, until the onions are soft and golden.",
    "Add the rice and white wine and cook until the liquid is dissolved, stirring frequently.", "Add 2 to 3 cups of the shrimp cooking water to the rice.", "Cover and simmer over low heat until the rice has absorbed the water and is fully cooked, about 15 minutes. Add more liquid if needed.",
    "Just before the rice is done, add frozen peas if desired.", "Taste the mixture and season with salt and pepper as desired.", "Remove from the heat and add the cooked shrimp.", "Garnish with minced cilantro and lime juice."]

    shrimp_paella=models.Recipe(name_displayed="Peruvian Shrimp Paella", food_name="shrimp_paella", ingredients=ingredients6_array, directions=directions6_array, picture="/static/shrimppaella.png")
    shrimp_paella.put()

    ingredients7_array=["24 jumbo raw shrimp (about 2 pounds), peeled, deveined, and tails removed", "6 to 7 strips of bacon", "1 cup of Louisiana Hot Sauce (not Tabasco sauce)"]

    direction7_array=["Preheat the oven to 400 degrees F.", "Peel and devein the shrimp, remove the tails (if desired)", "Line a baking sheet with parchment paper and arrange bacon on the sheet. Bake the bacon until half-cooked (about 6 minutes). Remove from oven and let the bacon cool and slice each piece in half and then half the bacon pieces again.",
    "Wrap each bacon slice tightly around the center of each shrimp and secure with a toothpick.", "Arrange the shrimp back on baking sheet and bake until the bacon is cooked through and crispy, approximately 6 minutes. The shrimp will have also turned pink.", "Once cooked, transfer the shrimp to a large bowl and gently toss with the Louisiana Hot Sauce until each piece is well coated."]

    buffalo_shrimp=models.Recipe(name_displayed="Bacon Wrapped Buffalo Shrimp", food_name="buffalo_shrimp", ingredients=ingredients7_array, directions=direction7_array, picture="/static/buffalo_shrimp.png")
    buffalo_shrimp.put()

    ingredients8_array=["3 pounds head-on large shrimp or 1 1/2 pounds tail-on large shrimp", "1/2 cup olive oil", "1/4 cup fresh breadcrumbs", "1 tablespoon (or to taste) minced garlic",
    "1/4 cup finely chopped parsley", "1 (14-ounce) can undrained peeled tomatoes, broken up", "1 teaspoon", "Vegeta seasoning (see Note, below)", "2 cups dry white wine", "Salt and pepper to taste"]

    directions8_array=["3 pounds head-on large shrimp or 1 1/2 pounds tail-on large shrimp", "1/2 cup olive oil", "1/4 cup fresh breadcrumbs", "1 tablespoon (or to taste) minced garlic", "1/4 cup finely chopped parsley", "1 (14-ounce) can undrained peeled tomatoes, broken up", "1 teaspoon Vegeta seasoning", "2 cups dry white wine", "Salt and pepper to taste"]

    croatian_shrimp=models.Recipe(name_displayed="Croatian Shrimp (Skampi Na Buzara)", food_name="croatian_shrimp", ingredients=ingrediants8_array, directions=directions8_array, picture="/static/croatian_shrimp.jpg")
    croatian_shrimp.put()

    ingredients9_array=["2 tablespoons oyster sauce", "2 tablespoon soy sauce", "2 tablespoons fresh cilantro minced (optional)", "2 teaspoons cornstarch", "1 pound shrimp peeled and deveined (tails left intact optional)", "2 tablespoons cooking oil divided", "3 green onion chopped (white and light green parts)",
    "2-3 garlic cloves finely minced", "2 teaspoons grated fresh ginger use microplane grater",]

    directions9_array=["2 tablespoons oyster sauce", "2 tablespoon soy sauce", "2 tablespoons fresh cilantro minced (optional)", "2 teaspoons cornstarch", "1 pound shrimp peeled and deveined (tails left intact optional)",
    "2 tablespoons cooking oil divided", "3 green onion chopped (white and light green parts)", "2-3 garlic cloves finely minced", "2 teaspoons grated fresh ginger use microplane grater"]

    shrimp_stirfry=models.Recipe(name_displayed="Chinese Shrimp Stir Fry", food_name="shrimp_stirfry", ingredients=ingredients9_array, directions=directions9_array, picture="/static/shrimp_stirfry.jpg")
    shrimp_stirfry.put()

    ingredients10_array=["3 medium serrano chiles", "4 medium garlic cloves", "1 tablespoon smoked paprika", "1/4 cup freshly squeezed lime juice", "1 tablespoon red wine vinegar", "1/2 cup olive oil", "1 1/2 pounds uncooked, deveined, and peeled shrimp, tails left on", "kosher salt", "1/3 cup roughly chopped fresh cilantro leaves", "Lime wedges", "Cooked white or brown rice"]

    directions10_array=["Heat oven to 500F and arrange rack in upper third. Place chiles on a baking sheet and roast until blackened and soft, about 10 to 15 minutes. (Alternatively roast them in a dry cast iron skillet over medium heat.) Set chiles aside to cool briefly then trim off stems, cut in half lengthwise, and remove the white ribs and seeds.",
    "Combine trimmed chiles, garlic, paprika, lime juice, and vinegar in a blender or mini food processor and blend until smooth and combined, about 1 minute. Add olive oil and blend until thoroughly incorporated and marinade thickens slightly. Combine marinade and shrimp in a medium nonreactive bowl and toss to coat. Let marinate 20 minutes to 24 hours in the refrigerator.",
    "Heat a large cast iron skillet over medium-high heat. When heated, add the shrimp and marinated and cook until the shrimp are pink. Season well with salt, toss shrimp with cilantro, and serve with lime wedges over rice."]

    piri_shrimp=models.Recipe(name_displayed="Piri-Piri Style Shrimp", food_name="piri_shrimp", ingredients=ingredients10_array, directions=directions10_array, picture="/static/piri_shrimp.png")
    piri_shrimp.put()

    ingredients11_array=["4 egg whites", "1/2teaspoon cream of tartar", "1cup sugar", "1pinch salt", "1/2teaspoon vanilla", "1 Sponge cake recipe, baked in two 9-inch cake pans", "6 or 7 peaches",
    "1cup sugar", "1cup water", "1teaspoon vanilla", "1pinch salt"]

    directions11_array=["Preheat oven to 200F.", "Prepare the meringue: Beat the egg whites and cream of tartar until stiff peaks start to form. Gradually add the sugar and continue to beat until peaks are very stiff and sugar is dissolved. Beat in the vanilla and a pinch of salt.",

    "Bake meringue pieces for at least and hour and a half, until they are dry and completely crispy. Keep meringues in an airtight container or closed oven until ready to use.", "Prepare sponge cake recipe or angel food cake in two 9 inch cake pans and bake. Cool completely in pans, then remove carefully.",
    "Peel and slice peaches, and place sliced peaches in a stainer over a bowl. Toss peach slices with 1-2 tablespoons of sugar. Let peaches rest for about 20 minutes, reserving the peach juice that drains into the bowl.", "Bring 1 cup water, 1 cup sugar, and reserved peach juice to a boil, and simmer until sugar is dissolved. Remove from heat and let cool. Stir in vanilla, pinch of salt, and optional rum or vodka, if desired.",
    "Stir 2 tablespoons sugar into the whipping cream and whip until medium stiff peaks form. Stir vanilla into the whipped cream, and refrigerate until ready to assemble cake.", "To assemble cake: Flip sponge cakes upside down and brush each cake generously with the peach syrup, soaking the cakes."]

    peach_meringuecake=models.Recipe(name_displayed="Postre Chaja Peach Meringue Cake", food_name="peach_meringuecake", ingredients=ingredients11_array, directions=directions11_array, picture="/static/peach_meringuecake.jpg")
    peach_meringuecake.put()

    ingredients12_array=["1/2 cup melted butter", "1 cup flour", "1 cup sugar", "2 teaspoons baking powder", "1/4 teaspoon salt", "2/3 cup room temperature milk", "1 room temperature egg", "1(28 ounce) cansliced peaches, drained", "1 cup sugar", "1 teaspoon cinnamon", "1/2 teaspoon nutmeg"]

    directions12_array=["Melt butter in a 9 x 13 inch pan.", "Mix together flour, sugar, baking powder & salt.", "Stir in milk & egg.", "Pour evenly over melted butter.", "Combine peaches, sugar & spices and spread over batter-DO NOT STIR!", "Bake 35-45 minutes at 350F until batter comes to the top and is golden brown."]

    peach_cobbler=models.Recipe(name_displayed="Peach Cobbler", food_name="peach_cobbler", ingredients=inngredients12_array, directions=directions12_array, picture="/static/peach_cobbler.png")
    peach_cobbler.put()

    ingredients13_array=["10 peaches, pitted, pealed, and cut into quarters", "1 lb. cottage cheese", "1/2 C. butter", "4 eggs, slightly beaten", "2 T. farina", "1/2 C. flour"]

    directions13_array=["In a large bowl, beat together the cheese and butter until well blended. Add in the eggs, farina and flour and mix until a dough forms. Cut off ping-pong sized pieces of dough and pat to round, 1/4 inch thick pieces. Place a piece of peach in the center of the dough, then seal the edges around the fruit, into a ball.", "Bring a large pot of water to boil. Gently place each dumpling into the water, cover the pot and cook for 10 minutes, or until the dumplings rise to the top.", "Drain, and sprinkle with bread crumbs, melted butter, or chopped nuts"]

    peach_dumplings=models.Recipe(name_displayed="Gooey Peach Dumplings", food_name="peach_dumplings", ingredients=ingredients13_array, directions=directions13_array, picture="/static/peach_dumplings.png"
    peach_dumplings.put()

    ingredients14_array=["1 tablespoon canola oil", "4 skinless, boneless chicken breasts, about 1 1/4 pounds", "1/2 teaspoon salt", "1/4 teaspoon pepper", "2 tablespoons brown sugar", "2 tablespoons low-sodium soy sauce", "2 tablespoons rice vinegar",
    "1/4 cup orange juice", "1 teaspoon freshly grated ginger", "2 cloves garlic, minced", "1/2 cup low-sodium chicken broth", "4 large firm-ripe peaches, cut into 1/4-inch slices, or 2 (10-ounce) packages frozen peaches, (about 4 1/2 cups)", "2 tablespoons sliced almonds"]

    directions14_array=["Heat the oil in a large skillet over a medium-high heat. Season the chicken on both sides with salt and pepper, add to the skillet and cook until browned, about 2 minutes per side. Meanwhile combine the brown sugar, soy sauce, rice vinegar and orange juice in a small bowl and set aside. When the chicken is browned, transfer to a plate and set aside.",
    "Add the ginger and garlic to the pan and cook, stirring, for 30 seconds. Add the chicken broth, the soy sauce mixture, and the peaches to the pan. Turn the heat up to high and cook, uncovered, for about 6 minutes, stirring occasionally until the sauce is nicely thickened and the peaches soften. Add the chicken back to the pan with the sauce, turn the heat down to moderate-low, cover and cook for about 5 minutes, or until chicken is cooked through.",
    "In the meantime, toast the almonds in a dry skillet over a medium-high heat stirring frequently, until golden brown and fragrant, about 2 minutes.", "Serve the chicken topped with the sauce and sprinkled with the toasted almonds."]

    peach_chicken=models.Recipe(name_displayed="Peach Chicken", food_name="peach_chicken", ingredients=ingredients14_array, directions=directions14_array, picture="/static/peach_chicken.jpeg")
    peach_chickn.put()

    ingredients15_array=["1/4 cup rice", "3 cup of milk", "3/4 cup sugar", "1 tin of KOO peach slices", "1/2 tsp corn flour", "1/2 teaspoon cardamom powder"]

    directions15_array=["Wash & soak rice after wash for about 20 minutes", "Drain the water after the soak & blend the rice to fine texture adding milk as needed to make it smooth", "Drain the syrup from the canned peaches, keep a few slices aside for the garnish.", "Puree the remaining peaches with the corn flour in a blender & keep aside.", "Boil milk on medium heat for 8 minutes & let it reduce.",
    "Take 1/4 cup of hot milk & mix it into the rice mixture.", "Add the rice paste to the boiling milk slowly & continue stirring making sure it does not burn at the bottom.", "Cook until milk has reduced & rice is cooked.", "Add sugar & cardamom to the mixture & continue cooking for about 4 minutes on low heat then turn off heat.", "Fold in the pureed peach mixture, do not stir only fold it in & dish into little desert bowls.",
    "Refrigerate for 2 hours & then garnish with sliced almond, peach slices & mint leaves.", "Discover more African and Caribbean recipes on Demand Africa"]

    peach_phirini=models.Recipe(name_displayed="Peach Phirini", food_name="peach_phirini", ingredients=ingredients15_array, directions=directions15_array, picture="/static/")
    peach_phirini.put()


# def get_link_url (url):
#     if url=="/recipes/firstrecipe":
#         namefood="apple_pie"
#     elif url=="/recipes/secondrecipe":
#         namefood="apple_empanadas"
#     elif url=="/recipes/thirdrecipe":
#         namefood="danish_apple_pie"
#     elif url=="/recipes/fourthrecipe":
#         namefood="apple_slaw"
#     elif url=="/recipes/fifthrecipe":
#         namefood="apple_tart"
#     else:
#         namefood="nothing"
#     return namefood
