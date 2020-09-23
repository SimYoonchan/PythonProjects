import shelve

with shelve.open('hangman library') as hangman_library:
    hangman_library['Countries'] = ["Afghanistan", "Albania", "Algeria",
                                    "Andorra", "Angola", "Argentina",
                                    "Armenia", "Australia", "Austria",
                                    "Azerbaijan",

                                    "Bahamas", "Bahrain", "Bangladesh",
                                    "Barbados", "Belarus", "Belgium",
                                    "Belize", "Benin", "Bhutan",
                                    "Bolivia", "Botswana", "Brazil",
                                    "Brunei", "Bulgaria", "Burkina Faso",
                                    "Burma", "Burundi",

                                    "Cambodia", "Cameroon", "Canada",
                                    "Cape Verde", "Central African Republic",
                                    "Chad", "Chile", "China", "Comoros",
                                    "Congo", "Costa Rica", "Côte d'Ivoire",
                                    "Croatia", "Cuba", "Cyprus",
                                    "Czech Republic"

                                    "Denmark", "Djibouti", "Dominican Republic",

                                    "East Timor", "Ecuador", "Egypt",
                                    "El Salvador", "Equatorial Guinea",
                                    "Eritrea", "Estonia", "Eswatini",
                                    "Ethiopia",

                                    "Fiji", "Finland", "France",

                                    "Gabon", "Georgia", "Germany",
                                    "Ghana", "Greece", "Grenada", "Guatemala",
                                    "Guyana",

                                    "Haiti", "Honduras", "Hungary",

                                    "Iceland", "India", "Indonesia", "Iran",
                                    "Iraq", "Ireland", "Israel", "Italy",

                                    "Jamaica", "Japan", "Jordan",

                                    "Kazakhstan", "Kenya", "Kiribati",
                                    "North Korea", "South Korea", "Kuwait",
                                    "Kyrgyzstan",

                                    "Laos", "Latvia", "Lebanon", "Lesotho",
                                    "Liberia", "Libya", "Liechtenstein",
                                    "Lithuania", "Luxembourg",

                                    "Macedonia", "Madagascar", "Malawi",
                                    "Malaysia", "Maldives", "Mali",
                                    "Malta", "Marshall Islands",
                                    "Mauritania", "Mauritius", "Mexico",
                                    "Micronesia", "Moldova", "Monaco",
                                    "Mongolia", "Montenegro", "Morocco",
                                    "Mozambique",

                                    "Namibia", "Nauru", "Nepal", "Netherlands",
                                    "New Zealand", "Nicaragua", "Niger",
                                    "Nigeria", "Norway",

                                    "Oman",

                                    "Pakistan", "Palau", "Panama",
                                    "Papua New Guinea", "Paraguay", "Peru",
                                    "Philippines", "Poland", "Portugal",

                                    "Qatar",

                                    "Romania", "Russia", "Rwanda",

                                    "Saint Kitts and Nevis", "Saint Lucia",
                                    "Saint Vincent and the Grenadines",
                                    "Samoa", "San Marino", "Saudi Arabia",
                                    "São Tomé and Príncipe", "Senegal",
                                    "Serbia", "Seychelles", "Sierra Leone",
                                    "Singapore", "Slovakia", "Slovenia",
                                    "Solomon Islands", "Somalia",
                                    "South Africa", "Spain", "Sri Lanka",
                                    "Sudan", "Suriname", "Sweden", "Switzerland",
                                    "Syria",

                                    "Tajikistan", "Tanzania", "Thailand",
                                    "The Gambia", "Togo", "Tonga", "Trinidad and Tobago",
                                    "Tunisia", "Turkey", "Turkmenistan",
                                    "Tuvalu",

                                    "Uganda", "Ukraine", "United Arab Emirates",
                                    "United Kingdom", "United States of America",
                                    "Uruguay", "Uzbekistan",

                                    "Vanuatu", "Vatican City", "Venezuela",
                                    "Vietnam",

                                    "Yemen",

                                    "Zambia", "Zimbabwe"
                                    ]
    hangman_library['Dogs'] = ["Afghan hound", "African wild dog", "Airedale terrier",
                               "Akita", "Alaskan malamute", "American cocker spaniel",
                               "Australian cattle dog",

                               "basenji", "basset hound", "beagle",
                               "bergamasco","bichon frise", "bird dog",
                               "bloodhound", "border collie", "borzoi",
                               "Boston terrier", "boxer", "briard", "Brittany",
                               "bull terrier", "bulldog", "bullmastiff",

                               "cairn terrier", "Cape hunting dog",
                               "chihuahua", "Chinese crested dog",
                               "cocker spaniel", "collie", "coon hound",
                               "corgi",

                               "dachshund", "Dalmatian", "dingo", "Doberman pinscher",

                               "elkhound",

                               "fox terrier", "foxhound",

                               "German shepherd", "golden retriever",
                               "great Dane", "great Pyrenees", "greyhound",

                               "harrier", "husky",

                               "Irish setter",

                               "Jack Russell terrier",

                               "keeshondkerry blue terrier", "King Charles spaniel",

                               "Labrador retriever", "Lhasa apso",

                               "malamute", "Maltese", "mastiff",
                               "Mexican hairless", "miniature schnauzer",
                               "mongrel",

                               "Newfoundland", "Norfolk terrier",

                               "old English sheepdog",

                               "papillon", "pedigree", "pekingese", "pinscher",
                               "pit bull", "Pomeranian", "poodle", "Portuguese water dog",

                               "rat terrier", "Rhodesian ridgeback", "Rottweiler",

                               "Saluki", "schnauzer", "Scottish terrier",
                               "Siberian husky", "springer spaniel", "St. Bernard",

                               "utonagan",

                               "vizsla",

                               "weimaraner", "Welsh corgi", "West Highland white terrier",
                               "wheaten terrier",

                               "Yorkshire terrier"
                               ]
