"""Seed beginner breed + food + care guide data."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pet_world.settings')
django.setup()

from breeds.models import Breed
from care.models import FoodGuide, CareTip

BREEDS = [
    {
        'name': 'Golden Retriever',
        'pet_type': 'dog',
        'temperament': 'Friendly, loyal, patient',
        'size': 'Large',
        'lifespan': '10–12 years',
        'good_for_beginners': True,
        'overview': 'Golden Retrievers are calm family dogs and a great choice if you are new to pets. They love people and are easy to train with kindness.',
        'daily_care': 'Give 1–2 walks daily, brush coat 2–3 times a week, play fetch, and keep a clean sleeping area. Spend time talking and training with short sessions.',
        'food_guide': 'Feed good quality dog food twice a day. Puppies need 3 meals. Portion depends on age/weight — follow pack guide. You can add plain boiled chicken and rice sometimes.',
        'avoid_food': 'Never give chocolate, grapes, raisins, onion, garlic, xylitol (sugar-free gum), cooked bones, or too much oily junk food.',
        'common_mistakes': 'Overfeeding because they look hungry, skipping walks, and using harsh punishment. Use treats and praise instead.',
        'fun_fact': 'They were bred to gently retrieve birds without biting them.',
    },
    {
        'name': 'Beagle',
        'pet_type': 'dog',
        'temperament': 'Curious, playful, food-loving',
        'size': 'Small–Medium',
        'lifespan': '12–15 years',
        'good_for_beginners': True,
        'overview': 'Beagles are compact, happy dogs. Beginners should know they follow smells and need secure walks.',
        'daily_care': 'Walk twice daily on leash, give sniffing time, keep toys ready, and check ears weekly because they can get dirty.',
        'food_guide': '2 meals of dog kibble per day. Measure food carefully — Beagles gain weight easily. Healthy snacks: carrot sticks, apple slices (no seeds).',
        'avoid_food': 'Chocolate, onion, garlic, grapes, raisins, spicy human leftovers, and unlimited treats.',
        'common_mistakes': 'Leaving food open (they steal snacks) and walking without a strong leash/harness.',
        'fun_fact': 'Their nose is one of the strongest among dog breeds.',
    },
    {
        'name': 'German Shepherd',
        'pet_type': 'dog',
        'temperament': 'Smart, protective, active',
        'size': 'Large',
        'lifespan': '9–13 years',
        'good_for_beginners': False,
        'overview': 'Very intelligent working dogs. Better if you can give training time and exercise every day. Not ideal as a first “easy” pet unless you are ready.',
        'daily_care': 'Long walks + training games daily. Brush coat, clean ears, and give mental work (commands, puzzle toys).',
        'food_guide': 'High-quality dog food twice daily. Large-breed formula is better for joints. Keep fresh water always available.',
        'avoid_food': 'Chocolate, cooked bones, onion, garlic, grapes, and sudden random diet changes.',
        'common_mistakes': 'Keeping them locked with no activity — boredom can cause barking and chewing.',
        'fun_fact': 'They excel in police, rescue, and service work.',
    },
    {
        'name': 'Persian Cat',
        'pet_type': 'cat',
        'temperament': 'Calm, gentle, indoor-friendly',
        'size': 'Medium',
        'lifespan': '12–17 years',
        'good_for_beginners': True,
        'overview': 'Persians are quiet cats that enjoy a peaceful home. Perfect if you want a soft companion and can brush them regularly.',
        'daily_care': 'Brush fur daily to avoid tangles, clean eye corners gently, keep litter box clean, and provide a cozy resting spot.',
        'food_guide': 'Cat food (wet + dry mix works well) twice a day. Choose food for indoor cats. Occasional plain boiled chicken is fine.',
        'avoid_food': 'Onion, garlic, chocolate, milk (many cats can’t digest it), grapes, raisins, and dog food as main diet.',
        'common_mistakes': 'Skipping brushing (mats form fast) and ignoring litter cleanliness.',
        'fun_fact': 'Their flat faces need extra face cleaning care.',
    },
    {
        'name': 'Siamese Cat',
        'pet_type': 'cat',
        'temperament': 'Talkative, smart, social',
        'size': 'Medium',
        'lifespan': '12–20 years',
        'good_for_beginners': True,
        'overview': 'Siamese cats love attention and “talk” a lot. Good for owners who can spend time with them.',
        'daily_care': 'Play with wand toys daily, give climbing space, talk to them, and keep claws trimmed carefully.',
        'food_guide': 'Measured cat meals 2 times a day. High-protein cat food is best. Don’t free-feed unlimited dry food.',
        'avoid_food': 'Chocolate, onion, garlic, raw fish often, milk as routine drink, and bones.',
        'common_mistakes': 'Leaving them alone all day with no play — they can get lonely and loud.',
        'fun_fact': 'They are one of the most vocal cat breeds.',
    },
    {
        'name': 'Budgie (Parakeet)',
        'pet_type': 'bird',
        'temperament': 'Social, cheerful, active',
        'size': 'Small',
        'lifespan': '5–10 years',
        'good_for_beginners': True,
        'overview': 'Budgies are one of the best starter birds. They need clean cage, company, and daily interaction.',
        'daily_care': 'Refresh food/water daily, clean cage often, give toys, and let supervised out-of-cage time if safe.',
        'food_guide': 'Budgie seed mix + pellets. Add leafy greens, carrot, apple (small pieces). Cuttlebone for calcium.',
        'avoid_food': 'Avocado, chocolate, caffeine, salty chips, onion, garlic, and apple seeds.',
        'common_mistakes': 'Only seeds forever (unbalanced) and keeping cage in kitchen with smoke/strong smells.',
        'fun_fact': 'Males can often learn simple whistles and words.',
    },
    {
        'name': 'Cockatiel',
        'pet_type': 'bird',
        'temperament': 'Gentle, musical, affectionate',
        'size': 'Small–Medium',
        'lifespan': '10–15 years',
        'good_for_beginners': True,
        'overview': 'Cockatiels are friendly birds that bond with owners. Great if you want a pet that whistles and sits nearby.',
        'daily_care': 'Clean water every day, offer baths/misting, spend calm talking time, and keep cage away from drafts.',
        'food_guide': 'Pellets as base + limited seeds, veggies like spinach/carrot, and millet spray as occasional treat.',
        'avoid_food': 'Avocado, chocolate, caffeine, alcohol, salty food, and sticky soft bread as main food.',
        'common_mistakes': 'Too many sunflower seeds (fatty) and no social time.',
        'fun_fact': 'They can copy household sounds and simple tunes.',
    },
    {
        'name': 'Holland Lop Rabbit',
        'pet_type': 'other',
        'temperament': 'Sweet, quiet, cuddly',
        'size': 'Small',
        'lifespan': '7–12 years',
        'good_for_beginners': True,
        'overview': 'Rabbits are gentle pets but need correct food and space. Good for calm homes ready for daily cleaning.',
        'daily_care': 'Provide hay always, clean litter area, gentle handling, and supervised playtime outside cage.',
        'food_guide': 'Unlimited grass hay (main food), limited pellets, and leafy greens daily. Fresh water always.',
        'avoid_food': 'Chocolate, iceberg lettuce in large amounts, sugary treats, and sudden big diet changes.',
        'common_mistakes': 'Thinking carrots should be main food — carrot is only a small treat.',
        'fun_fact': 'Their teeth grow continuously, so hay is essential.',
    },
]

FOODS = [
    {
        'pet_type': 'dog',
        'title': 'Dog Food Basics',
        'daily_meals': '2 meals/day (puppies: 3)',
        'good_foods': 'Quality dog kibble, plain boiled chicken, rice, pumpkin, carrot, apple (no seeds), cucumber, dog-safe treats.',
        'bad_foods': 'Chocolate, xylitol, grapes, raisins, onion, garlic, alcohol, cooked bones, spicy leftovers, too much salt.',
        'feeding_tips': 'Keep a fixed schedule. Use a measuring cup. If changing food, mix old+new for 5–7 days. Don’t give food from your plate every time.',
        'water_tips': 'Always keep clean water. Wash bowl daily, especially in hot weather.',
    },
    {
        'pet_type': 'cat',
        'title': 'Cat Food Basics',
        'daily_meals': '2 meals/day (or wet morning + dry evening)',
        'good_foods': 'Cat wet food, cat dry food, plain cooked chicken/turkey, occasional boiled egg. Cats need animal protein.',
        'bad_foods': 'Onion, garlic, chocolate, grapes, raisins, dog food as main diet, milk for lactose-intolerant cats, raw fish often.',
        'feeding_tips': 'Prefer cat-specific food. Watch weight. If kitten, use kitten formula food. Keep food away from litter box.',
        'water_tips': 'Many cats like running water. A clean bowl or pet fountain helps prevent dehydration.',
    },
    {
        'pet_type': 'bird',
        'title': 'Bird Food Basics',
        'daily_meals': 'Fresh food daily + clean water always',
        'good_foods': 'Species pellets, seed mix in limits, leafy greens, carrot, apple/pear pieces, millet spray as treat, cuttlebone.',
        'bad_foods': 'Avocado, chocolate, caffeine, alcohol, salty chips, onion, garlic, apple seeds, junk fried food.',
        'feeding_tips': 'Don’t give only seeds. Add veggies daily. Remove uneaten fresh food after a few hours to avoid spoilage.',
        'water_tips': 'Change water every day. Use a clean drinker and rinse algae/slime often.',
    },
    {
        'pet_type': 'other',
        'title': 'Rabbit & Small Pet Food Basics',
        'daily_meals': 'Hay always available + greens daily',
        'good_foods': 'Grass hay (timothy/meadow), leafy greens, limited pellets, tiny fruit treats only sometimes.',
        'bad_foods': 'Chocolate, sticky sweets, too many carrots, iceberg lettuce as main food, sudden new foods in big amounts.',
        'feeding_tips': 'Hay should be 80%+ of diet. Introduce new greens slowly. Keep feeding area clean and dry.',
        'water_tips': 'Use a bottle or heavy bowl and check it works every day.',
    },
]

TIPS = [
    {
        'title': 'First Day With a New Pet',
        'level': 'beginner',
        'pet_type': '',
        'summary': 'Don’t force your pet on day one. Let them settle into the home.',
        'steps': 'Prepare food, water, bed/cage before bringing pet home.\nKeep the room quiet for the first day.\nLet the pet explore slowly.\nOffer food and water, but don’t panic if appetite is low at first.\nBook a vet checkup within the first week.',
    },
    {
        'title': 'Daily Routine Checklist',
        'level': 'daily',
        'pet_type': '',
        'summary': 'Check these 5 things every day to keep your pet healthy.',
        'steps': 'Fresh water\nCorrect meal on time\nToilet/litter/cage cleaning\nShort play or walk\nQuick health check (energy, eyes, appetite)',
    },
    {
        'title': 'Home Setup for Beginners',
        'level': 'home',
        'pet_type': '',
        'summary': 'Make your home safe before bringing a new pet.',
        'steps': 'Hide electric wires and small choking items.\nKeep cleaning chemicals closed.\nMake one quiet corner for sleeping.\nBuy basic kit: food bowl, water bowl, brush, waste bags/litter.\nKeep emergency vet number saved in phone.',
    },
    {
        'title': 'When to Visit the Vet',
        'level': 'health',
        'pet_type': '',
        'summary': 'Don’t ignore small problems — seeing a vet early is better.',
        'steps': 'No eating/drinking for many hours\nVomiting or diarrhea\nBreathing difficulty\nInjury or bleeding\nSudden low energy or hiding all day',
    },
    {
        'title': 'Dog Walking Basics',
        'level': 'daily',
        'pet_type': 'dog',
        'summary': 'Walks are important for both health and behavior.',
        'steps': 'Use a proper leash/collar or harness.\nStart with short walks if puppy/new dog.\nCarry water in hot weather.\nAvoid unknown street food leftovers.\nReward calm walking with praise.',
    },
    {
        'title': 'Cat Litter Box Rules',
        'level': 'daily',
        'pet_type': 'cat',
        'summary': 'Clean litter = happy cat. Dirty box causes accidents.',
        'steps': '1 litter box per cat + 1 extra if possible.\nScoop waste daily.\nWash box weekly.\nKeep box in quiet accessible place.\nDon’t place food next to litter.',
    },
]


def run():
    for data in BREEDS:
        obj, created = Breed.objects.update_or_create(
            name=data['name'],
            defaults=data,
        )
        print(('Created' if created else 'Updated'), 'breed:', obj.name)

    for data in FOODS:
        obj, created = FoodGuide.objects.update_or_create(
            pet_type=data['pet_type'],
            defaults=data,
        )
        print(('Created' if created else 'Updated'), 'food:', obj.title)

    for data in TIPS:
        obj, created = CareTip.objects.update_or_create(
            title=data['title'],
            defaults=data,
        )
        print(('Created' if created else 'Updated'), 'tip:', obj.title)

    print('TOTAL breeds:', Breed.objects.count())
    print('TOTAL foods:', FoodGuide.objects.count())
    print('TOTAL tips:', CareTip.objects.count())


if __name__ == '__main__':
    run()
