-- Adding myself as first user
INSERT INTO users(username, fullname, email, filename, alt, password)
VALUES
    ('igiallan', 'Isabella Giallanza', 'igiallan@umich.edu', 'Image of Isabella Giallanza', 'users/igiallan.jpg', 'password'),
    ('orozcoen', 'Enrique Orozco', 'orozcoen@umich.edu', 'Image of Enrique Orozco', 'users/orozcoen.jpeg', 'password');

-- Adding all pets
INSERT INTO pets(petid, petname, filename, alt, owner) 
VALUES
    (1, 'Bacon Q Dog', 'bacon/bacon.jpg', 'Brown labradoodle wearing colorful lei','igiallan'),
    (2, 'Fitz', 'fitz/Fitz.jpeg', 'Boston terrior watching a tennis ball at the table','igiallan'),
    (3, 'Pluto', 'pluto/pluto.jpg', 'White dog looking up.', 'orozcoen'),
    (4, 'Sage', 'sage/sage_classic.jpeg', 'A smiling golden retriever lying on the bed', 'igiallan'),
    (5, 'Smoothie', 'smoothie/Smoothie_staring.jpg', 'Long-hair beautiful, orange tabby cat', 'orozcoen');

-- Adding all pet likes
INSERT INTO pet_likes(petlikeid, petid, text)
VALUES
    (1, 1, 'Belly rubs'),
    (2, 1, 'playing tug-of-war'),
    (3, 1, 'sneaking onto the couch'),
    (4, 2, 'Blankets'),
    (5, 2, 'being warm'),
    (6, 2, 'barking'),
    (7, 3, 'Eating his bone'),
    (8, 3, 'going to the beach'),
    (9, 3, 'his toy duck'),
    (10, 4, 'Carrot'),
    (11, 4, 'nap'),
    (12, 4, 'big park'),
    (13, 5, 'Playing'),
    (14, 5, 'sunshine');

-- Adding all pet blurbs
INSERT INTO pet_blurbs(petblurbid, petid, text)
VALUES
    (1, 1, 'Bacon Q. Dog is a 9yr old labradoodle. He prefers to spend his days lounging among the three different beds/couches that his family has gifted him. He enjoys a walk or two around the neighborhood, as long as he can pretend that he doesn''t see any of the other animals to avoid the embarrassment of not wanting to admit he has no wolf-like skills in chasing them.'),
    (2, 1, 'At night just as the rest of the family is ready to relax, Bacon suddenly wants to release all of his energy. He will place his toys on a mini couch and frantically drag the couch around, giving his toys "a ride." There is also a lot of rolling. Lots and lots of rolling.'),
    (3, 2, 'Fitz is a boston terrior. He loves chasing tennis balls, chipmunks, squirrels, and birds. He is often found sitting by the fire in wintertime and in sun patches when available. He''s energetic, mischievious, and easily bored. He loves people and gets grumpy if left without a lap too long.'),
    (4, 2, 'Fitz loves barking up trees, running aorund on the lawn, and digging in the dirt looking for moles. He especially likes getting treats and whines when he comes inside and doesn''t get a snack.'),
    (5, 3, 'Pluto is a five year old rescue dog of an unknown breed. He was found wandering alone and taken to the Valley Humane Society where he found his new family. From a young age, Pluto always had a special personality, he was known for being very very lazy! He spends most of his time staring out the window to keep watch of his house. Don''t let the laziness fool you because Pluto defends his family from the mailman and squirrels every single day.'),
    (6, 3, 'Aside from his job as defender of the house, Pluto likes to have fun. Pluto''s favorite part of the day is his daily walk. Sometimes he even gets to go to the park and meet his neighbors. He also loves his toy duck, and only his toy duck. As a dog, it''s in his nature to hunt and so he makes sure to get some practice with his toy duck.'),
    (7, 4, 'Sage is a 3 year old Golden Retriever. She is one of the laziest dogs. She loves sneaking into the bedroom and hopping onto the neatest bed. She also loves riding in a car with the windows open feeling the wind and air. She enjoys walking, only if you take her for a ride to a big arboretum or park. Walking around the neighborhood is not necessarily her cup of tea.'),
    (8, 4, 'Her favorite food is corn. One day, she stole corn on the cob from the dining table, which was surprising because she is normally gentle and polite. She took the stolen corn to the patio and enjoyed her meal by herself. Unfortunately, the corn turned out to be unripe, so she ended up vomiting it all later.'),
    (9, 5, 'Smoothie has been dubbed the "world''s most photogenic cat", and her emerald eyes and golden fur have even inspired a mural in New Zealand. Smoothie also has an aptly-named brother named Milkshake, and the two are often featured together across social media platforms.'),
    (10, 5, 'She became an internet sensation with 2.3 million followers on her smoothiethecat Instagram account.');

-- Adding all pet media images
INSERT INTO pet_media(petmediaid, petid, filename, alt)
VALUES
    (1, 1, 'bacon/bacon_bandana.JPG', 'Brown labradoodle wearing an orange bandana'),
    (2, 1, 'bacon/bacon_graduation.JPG', 'Small labradoodle puppy wearing a graduation cap and gown'),
    (3, 1, 'bacon/bacon_agility.mov', 'Video of bacon being agile'),
    (4, 1, 'bacon/bacon_halloween.JPG', 'Brown labradoodle wearing a pirate costume'),
    (5, 2, 'fitz/Fitz_standing_on_chair.jpeg', 'Fitz standing on a wooden chair, looking at the camera.'),
    (6, 2, 'fitz/Fitz_sleeping.jpeg', 'Fitz sleeping in a fuzzy dog bed.'),
    (7, 2, 'fitz/Fitz_on_the_lawn.jpeg', 'Fitz laying out on the lawn in the grass.'),
    (8, 2, 'fitz/Fitz_laying_in_bed.jpeg', 'Fitz sleeping with his face buried in a plaid blanket, only his head is visible.'),
    (9, 3, 'pluto/pluto_cookie.JPG', 'Pluto the dog standing up to eat a cookie.'),
    (10, 3, 'pluto/pluto_sleeping.jpg', 'Pluto sleeping on the bed.'),
    (11, 3, 'pluto/pluto_walk.jpg', 'Pluto the dog on a walking trail.'),
    (12, 3, 'pluto/pluto_sitting.jpg', 'Pluto sitting and posed on top of a table'),
    (13, 4, 'sage/sage_young.jpeg', 'A young golden retriever is laying down'),
    (14, 4, 'sage/sage_car.jpeg', 'A happy golden retriever is sitting in the car''s backseat.'),
    (15, 4, 'sage/sage_sleep.jpeg', 'A golden retriever is sleeping on the couch.'),
    (16, 4, 'sage/sage_pet.jpeg', 'A man''s hand is petting a golden retriever''s neck.'),
    (17, 5, 'smoothie/Smoothie_yawn.jpg', 'Smoothie is yawning'),
    (18, 5, 'smoothie/Smoothie_lying.jpg', 'Smoothie is lying'),
    (19, 5, 'smoothie/Smoothie_staring.jpg', 'Smoothie is staring at you'),
    (20, 5, 'smoothie/Smoothie_curious.jpg', 'Smoothie is curious about the world');

-- Adding all recipes
INSERT INTO recipes(recipeid, recipename, origin, source, category, filename, alt, owner)
VALUES 
    (1, 'BLAT Sandwich', 'America', 'Yiran Zhang', 'main', 'blat/blat_main.png', 'Image of BLAT sandwich', 'igiallan'),
    (2, 'Guacamole', 'Mexico', 'Yiran Zhang', 'Appetizer', 'guacamole/guacamole.jpg', 'Image of guacamole', 'orozcoen'),
    (3, 'Chinese Jiaozi', 'China', 'flour, pork, and cabbage', 'main', 'jiaozi/jiaozi.jpeg', 'Image of jiaozi', 'igiallan');

-- Adding all recipe blurbs
INSERT INTO recipe_blurbs(recipeblurbid, recipeid, text)
VALUES
    (1, 1, 'A BLAT sandwich is a delicious twist on the classic BLT, featuring crispy bacon, fresh lettuce, ripe tomatoes, and creamy avocado, all sandwiched between slices of bread for a satisfying blend of flavors and textures.'),
    (2, 2, 'Guacamole is a Mexican dip made from mashed avocados, tomatoes, onions, cilantro, lime juice, and chili pepper, creating a creamy, zesty, and versatile condiment often enjoyed with tortilla chips, tacos, and more.'),
    (3, 3, 'Chinese dumplings (Jiaozi, 饺子) are stuffed parcels made of unleavened dough and savory fillings consisting of minced ingredients like meat, egg, tofu, or vegetables. They can be boiled, pan-fried or steamed.');

-- Adding all ingredients
INSERT INTO ingredients(ingredientid, recipeid, text)
VALUES
    (1, 1, 'Avocado'),
    (2, 1, 'Bacon'),
    (3, 1, 'Lettuce'),
    (4, 1, 'Tomato'),
    (5, 1, 'Bread'),
    (6, 1, 'Mayo'),
    (7, 2, 'Avocado'),
    (8, 2, 'Lime'),
    (9, 2, 'Salt'),
    (10, 2, 'Onion'),
    (11, 2, 'Tomato'),
    (12, 2, 'Cilantro'),
    (13, 3, 'Flour'),
    (14, 3, 'Water'),
    (15, 3, 'Pork'),
    (16, 3, 'Cabbage');

-- Adding all steps
INSERT INTO steps(stepid, recipeid, text)
VALUES
    (1, 1, 'Toasted bread slice spread with mayo'),
    (2, 1, 'Put sliced acovado, bacons, sliced tomatoes, lettuce on one spread of bread'),
    (3, 1, 'Put the other slice of bread at the top'),
    (4, 2, 'Slice three ripe avocados in half'),
    (5, 2, 'Scoop them into a mixing bowl'),
    (6, 2, 'Use a fork to gently mash them'),
    (7, 2, 'Add the onions, tomatoes, cilantro, jalapeno pepper, garlic, lime juice and salt and stir everything together.'),
    (8, 3, 'Dough'),
    (9, 3, 'Filling'),
    (10, 3, 'Folding'),
    (11, 3, 'Cooking'),
    (12, 3, 'Dipping sauces');

-- Adding all recipe media images
INSERT INTO recipe_media(recipemediaid, recipeid, filename, alt)
VALUES
    (1, 1, 'blat/ingredients.jpg', 'Ingredients of BLAT sandwich'),
    (2, 1, 'blat/blat_2.jpg', 'A BLAT sandwich is placed on a dish.'),
    (3, 1, 'blat/blat_3.jpg', 'A BLAT sandwich is made with multigrain bread.'),
    (4, 2, 'guacamole/avocado_chips.jpg', 'Chips and guacamole'),
    (5, 2, 'guacamole/taco.jpg', 'Guacamole in taco'),
    (6, 2, 'guacamole/guacamole_2.jpg', 'Guacamole in a bowl'),
    (7, 3, 'jiaozi/jiaozi2.jpeg', 'Three dishes of Jiaozi'),
    (8, 3, 'jiaozi/jiaozi3.jpeg', 'Steamed jiaozi'),
    (9, 3, 'jiaozi/jiaozi4.jpeg', 'Making jiaozi');

-- Adding all travels
INSERT INTO travel(travelid, travelname, location, owner)
VALUES
    (1, 'Yellowstone National Park', 'North America', 'igiallan'),
    (2, 'Hangzhou', 'Asia', 'igiallan'),
    (3, 'New York City', 'North America', 'igiallan');

-- Adding all travel mains
INSERT INTO travel_main(mainid, travelid, still, moving, alt)
VALUES
    (1, 1, 'yellowstone/yellowstone_cauldron.jpg', 'yellowstone/yellowstone_cauldron.gif', 'Yellowstone cauldron'),
    (2, 2, 'hangzhou/hangzhou_main.jpg', 'hangzhou/hangzhou.gif', 'Hangzhou main gif'),
    (3, 3, 'nyc/nyc_buildings.jpg', 'nyc/nyc.gif', 'NYC gif');

-- Adding all travel blurbs
INSERT INTO travel_blurbs(travelblurbid, travelid, text)
VALUES
    (1, 1, 'Yellowstone National Park is a national park located in the western United States, largely in the northwest corner of Wyoming and extending into Montana and Idaho. It was established by the 42nd U.S. Congress with the Yellowstone National Park Protection Act and signed into law by President Ulysses S. Grant on March 1, 1872. Yellowstone was the first national park in the U.S. and is also widely held to be the first national park in the world. The park is known for its wildlife and its many geothermal features, especially the Old Faithful geyser, one of its most popular. While it represents many types of biomes, the subalpine forest is the most abundant. It is part of the South Central Rockies forests ecoregion.'),
    (2, 1, 'Yellowstone National Park spans an area of 3,468.4 sq mi (8,983 km2), comprising lakes, canyons, rivers, and mountain ranges. Yellowstone Lake is one of the largest high-elevation lakes in North America and is centered over the Yellowstone Caldera, the largest super volcano on the continent. The caldera is considered a dormant volcano. It has erupted with tremendous force several times in the last two million years. Well over half of the world''s geysers and hydrothermal features are in Yellowstone, fueled by this ongoing volcanism. Lava flows and rocks from volcanic eruptions cover most of the land area of Yellowstone. The park is the centerpiece of the Greater Yellowstone Ecosystem, the largest remaining nearly intact ecosystem in the Earth''s northern temperate zone. In 1978, Yellowstone was named a UNESCO World Heritage Site.'),
    (3, 2, 'Hangzhou, situated in eastern China, is a city that seamlessly blends ancient heritage with natural splendor. At the heart of its allure lies the iconic West Lake, a UNESCO World Heritage Site celebrated for its picturesque landscapes. Here, serene waters mirror the surrounding lush gardens, historic temples, and quaint tea houses, creating a tranquil oasis in the heart of the city. West Lake has been an enduring muse for poets, scholars, and artists for centuries, offering a captivating escape where willow trees gracefully sway, lotus flowers bloom, and visitors can glide across its waters on paddle boats, connecting with the city''s deep-rooted love for nature.'),
    (4, 2, 'Hangzhou is also famous for its Longjing tea, a prized variety of green tea cultivated in the nearby rolling hills. Enthusiasts can partake in traditional tea ceremonies, explore centuries-old tea plantations, and gain insight into the meticulous art of tea production passed down through generations. This rich tea culture, alongside the city''s modernity and technological prowess, paints a vivid portrait of Hangzhou—a place where tradition harmonizes with innovation, making it a captivating destination for those seeking a glimpse into China''s multifaceted cultural heritage.'),
    (5, 3, 'New York City, often dubbed the "City that Never Sleeps," is a bustling metropolis like no other. Its iconic skyline, dominated by towering skyscrapers like the Empire State Building and One World Trade Center, symbolizes its ceaseless ambition and innovation. The city''s cultural diversity is a defining feature, with neighborhoods like Chinatown, Little Italy, and Harlem offering a rich tapestry of traditions and flavors. From the bright lights of Times Square to the tranquility of Central Park, New York City offers a striking blend of urban excitement and natural beauty. It''s a place where world-class museums, theaters, and restaurants cater to a global audience, making it a beacon for culture and creativity.'),
    (6, 3, 'Beyond the surface, New York City''s subway system and iconic yellow taxis make it remarkably accessible, allowing residents and visitors alike to explore its diverse offerings. This city is a stage for dreams to be pursued, a canvas for artistry to flourish, and a relentless engine of progress. It''s a place where the past meets the future, and where every corner seems to tell a unique story, making New York City an irresistible destination for those seeking inspiration and adventure.');

-- Adding all travel medias
INSERT INTO travel_media(travelmediaid, travelid, filename, alt, caption)
VALUES
    (1, 1, 'yellowstone/yellowstone_travertine.JPG', 'A large mound of multi-colored travertine', 'Mammoth Hot Springs has a number of actively forming Travertine terraces.'),
    (2, 1, 'yellowstone/yellowstone_prism.MOV', 'yellowstone prism', 'The multicolored layers get their hues from different species of bacteria living in the cooler water around the spring.'),
    (3, 1, 'yellowstone/yellowstone_buffalo.MOV', 'yellowstone buffalo', 'The multicolored layers get their hues from different species of bacteria living in the cooler water around the spring.'),
    (4, 1, 'yellowstone/yellowstone_sulphur_springs.JPG', 'A large spring with cloud of sulfut smoke rising from it.', 'If you can handle the odor, the Yellowstone Sulphur Springs is a great place to hike.'),
    (5, 2, 'hangzhou/westlake.jpg', 'Westlake jpg', 'West Lake is a UNESCO World Heritage Site in Hangzhou, China, celebrated for its serene waters, enchanting gardens, historic temples, and a profound cultural connection to classical Chinese landscapes.'),
    (6, 2, 'hangzhou/lingyin.jpg', 'Lingyin Temple', 'Lingyin Temple, located near West Lake in Hangzhou, is a renowned ancient Buddhist temple known for its rich history, intricate architecture, and serene natural surroundings.'),
    (7, 2, 'hangzhou/alibaba.jpeg', 'Alibaba Group jpg', 'Alibaba Group is a multinational conglomerate based in China, known for its e-commerce platforms, cloud computing services, and digital technology innovations, playing a pivotal role in shaping the global digital economy.'),
    (8, 3, 'nyc/brooklyn_bridge.jpg', 'Image of the Brooklyn Bridge', 'The Brooklyn Bridge is an iconic suspension bridge spanning the East River, connecting Manhattan and Brooklyn, known for its majestic architecture and historical significance.'),
    (9, 3, 'nyc/flatiron.jpg', 'Image of the Flatiron Building', 'The Flatiron Building, with its distinctive triangular shape and Beaux-Arts architecture, is a historic landmark nestled in the heart of Manhattan, epitomizing New York City''s architectural charm.'),
    (10, 3, 'nyc/central_park.jpg', 'Image of Central Park', 'Central Park is a sprawling urban oasis in the heart of Manhattan, offering a serene escape from the city''s hustle and bustle with its lush greenery, scenic waterways, and diverse recreational opportunities.');

-- Adding all following
INSERT INTO following(username1, username2)
VALUES
    ('orozcoen', 'igiallan');
    