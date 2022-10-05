# To run this random story generator script, from root directory:
#   1) cd into 'projects' then 
#   2) cd into 'Story Generator' then 
#   3) run the command 'python story_generator.py' 

import random

when = [
  "In ancient times", "A long long time ago", "A few years ago", 
  "A few months ago", "Couple of weeks ago", "Last few days ago", 
  "Yesterday", "Last night", "On 1st Jan", "On 2nd Feb", "On 3rd March"
]

who = [ 
  "an aardvark", "an albatross", "an alligator", "an alpaca", "an ant", "an anteater", "an antelope", "an ape", "an armadillo", "a donkey", "a baboon", "a badger", "a barracuda", "a bat", "a bear", "a beaver", 
  "a bee", "a bison", "a boar", "a buffalo", "a butterfly", "a camel", "a capybara", "a caribou", "a cassowary", "a cat", "a caterpillar", "a cattle", "a chamois", "a cheetah", "a chicken", "a chimpanzee", "a chinchilla", 
  "a chough", "a clam", "a cobra", "a cockroach", "a cod", "a cormorant", "a coyote", "a crab", "a crane", "a crocodile", "a crow", "a curlew", "a deer", "a dinosaur", "a dog", "a dogfish", "a dolphin", "a dotterel", "a dove", 
  "a dragonfly", "a duck", "a dugong", "a dunlin", "an eagle", "an echidna", "an eel", "an eland", "an elephant", "an elk", "an emu", "a falcon", "a ferret", "a finch", "a fish", "a flamingo", "a fly", "a fox", "a frog", "a gaur", 
  "a gazelle", "a gerbil", "a giraffe", "a gnat", "a gnu", "a goat", "a goldfinch", "a goldfish", "a goose", "a gorilla", "a goshawk", "a grasshopper", "a grouse", "a guanaco", "a gull", "a hamster", "a hare", "a hawk", "a hedgehog", 
  "a heron", "a herring", "a hippopotamus", "a hornet", "a horse", "a human", "a hummingbird", "a hyena", "an ibex", "an ibis", "a jackal", "a jaguar", "a jay", "a jellyfish", "a kangaroo", "a kingfisher", "a koala", "a kookabura", 
  "a kouprey", "a kudu", "a lapwing", "a lark", "a lemur", "a leopard", "a lion", "a llama", "a lobster", "a locust", "a loris", "a louse", "a lyrebird", "a magpie", "a mallard", "a manatee", "a mandrill", "a mantis", "a marten", 
  "a meerkat", "a mink", "a mole", "a mongoose", "a monkey", "a moose", "a mosquito", "a mouse", "a mule", "a narwhal", "a newt", "a nightingale", "an octopus", "an okapi", "an opossum", "an oryx", "an ostrich", "an otter", "an owl", 
  "an oyster", "a panther", "a parrot", "a partridge", "a peafowl", "a pelican", "a penguin", "a pheasant", "a pig", "a pigeon", "a pony", "a porcupine", "a porpoise", "a quail", "a quelea", "a quetzal", "a rabbit", "a raccoon", "a rail", 
  "a ram", "a rat", "a raven", "a red deer", "a red panda", "a reindeer", "a rhinoceros", "a rook", "a salamander", "a salmon", "a sand dollar", "a sandpiper", "a sardine", "a scorpion", "a seahorse", "a seal", "a shark", "a sheep", "a shrew", 
  "a skunk", "a snail", "a snake", "a sparrow", "a spider", "a spoonbill", "a squid", "a squirrel", "a starling", "a stingray", "a stinkbug", "a stork", "a swallow", "a swan", "a tapir", "a tarsier", "a termite", "a tiger", "a toad", "a trout", 
  "a turkey", "a turtle", "a viper", "a vulture", "a wallaby", "a walrus", "a wasp", "a weasel", "a whale", "a wildcat", "a wolf", "a wolverine", "a wombat", "a woodcock", "a woodpecker", "a worm", "a wren", "a yak", "a zebra" 
]

where = [
  "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas ", "Bahrain", "Bangladesh", 
  "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia (Plurinational State of)", "Bonaire, Sint Eustatius and Saba", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory ", 
  "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands ", "Central African Republic ", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands ", "Colombia", 
  "Comoros ", "Congo", "Congo ", "Cook Islands ", "Costa Rica", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czechia", "Côte d'Ivoire", "Denmark", "Djibouti", "Dominica", "Dominican Republic ", "Ecuador", 
  "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Falkland Islands  [Malvinas]", "Faroe Islands ", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "French Southern Territories ", "Gabon", 
  "Gambia ", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard Island and McDonald Islands", "Holy See ", "Honduras", "Hong Kong", 
  "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "South Korea", 
  "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic ", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands ", "Martinique", 
  "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia (Federated States of)", "Moldova ", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands ", "New Caledonia", "New Zealand", 
  "Nicaragua", "Niger ", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands ", "Norway", "Oman", "Pakistan", "Palau", "Palestine, State of", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines ", "Pitcairn", "Poland", "Portugal", "Puerto Rico", 
  "Qatar", "Republic of North Macedonia", "Romania", "Russia", "Rwanda", "Réunion", "Saint Barthélemy", "Saint Helena, Ascension and Tristan da Cunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin (French part)", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", 
  "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten (Dutch part)", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "South Sudan", 
  "Spain", "Sri Lanka", "Sudan ", "Suriname", "Svalbard and Jan Mayen", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
  "Turks and Caicos Islands ", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates ", "United Kingdom of Great Britain and Northern Ireland", "United States Minor Outlying Islands", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Viet Nam", "Virgin Islands", 
  "Virgin Islands (U.S.)", "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe", "Åland Islands" 
]

went = ['cinema', 'university','seminar', 'school', 'laundry', 'playground', 'shopping mall', 'fashion store', 'fast food restaurant', 'city hall', 'town hall', 'cookhouse', 'beach']

what = ['made a lot of friends', 'ate a burger', 'found a magical key', 'solved a mystery', 'wrote a book', 'discovered raw gems', 'ate delicious food']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(where) + ', went to the ' + random.choice(went) + ' and ' + random.choice(what))
