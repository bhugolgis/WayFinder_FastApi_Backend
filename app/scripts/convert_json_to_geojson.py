import json

# Input JSON data
data = [
	{
		"id": 749,
		"Locality_Name": "World Trade Center",
		"Latitude": "18.91467177",
		"Longitude": "72.8179129",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 750,
		"Locality_Name": "Maker Towers",
		"Latitude": "18.91740599",
		"Longitude": "72.81678683",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 751,
		"Locality_Name": "Colaba Market",
		"Latitude": "18.91972365",
		"Longitude": "72.82981662",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 752,
		"Locality_Name": "Hotel President, Mumbai",
		"Latitude": "18.91424266",
		"Longitude": "72.82103223",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 753,
		"Locality_Name": "Railway Colony",
		"Latitude": "18.91868916",
		"Longitude": "72.82719785",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 754,
		"Locality_Name": "Colaba Post Office Bus Stop",
		"Latitude": "18.91095508",
		"Longitude": "72.82057938",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 755,
		"Locality_Name": "Backbay Bus Depot",
		"Latitude": "18.91004716",
		"Longitude": "72.81660038",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 756,
		"Locality_Name": "Dhobi Ghat / Dr. Ambedkar Nagar",
		"Latitude": "18.9111994",
		"Longitude": "72.81902055",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 757,
		"Locality_Name": "Cuffe Parade Police Station",
		"Latitude": "18.91189839",
		"Longitude": "72.81816157",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 758,
		"Locality_Name": "Colaba Bus Station",
		"Latitude": "18.91394845",
		"Longitude": "72.8226423",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 759,
		"Locality_Name": "President Hotel",
		"Latitude": "18.91488724",
		"Longitude": "72.82204642",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 760,
		"Locality_Name": "Colaba Post Office Bus Stop",
		"Latitude": "18.91095508",
		"Longitude": "72.82057938",
		"Station": {
			"id": 1
		}
	},
	{
		"id": 761,
		"Locality_Name": "Mantralaya",
		"Latitude": "18.92703629",
		"Longitude": "72.82681134",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 762,
		"Locality_Name": "New Administration Building",
		"Latitude": "18.92671512",
		"Longitude": "72.8265719",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 763,
		"Locality_Name": "Vidhan Bhavan Building",
		"Latitude": "18.92618519",
		"Longitude": "72.82493214",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 764,
		"Locality_Name": "Manora MLA Hostel",
		"Latitude": "18.92322648",
		"Longitude": "72.82508136",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 765,
		"Locality_Name": "State Bank Of India",
		"Latitude": "18.92622094",
		"Longitude": "72.82603336",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 766,
		"Locality_Name": "Shipping Corporation",
		"Latitude": "18.92622094",
		"Longitude": "72.82603336",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 767,
		"Locality_Name": "The Institute of Science",
		"Latitude": "18.9260736",
		"Longitude": "72.83024507",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 768,
		"Locality_Name": "Mittal Towers",
		"Latitude": "18.92525612",
		"Longitude": "72.82495741",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 769,
		"Locality_Name": "Maker Chambers",
		"Latitude": "18.92498403",
		"Longitude": "72.82274104",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 770,
		"Locality_Name": "NCPA (National Centre for Performing Arts)",
		"Latitude": "18.92486818",
		"Longitude": "72.82017833",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 771,
		"Locality_Name": "Yashwantrao Chavan Centre",
		"Latitude": "18.92493752",
		"Longitude": "72.82652517",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 772,
		"Locality_Name": "Sachivalay Gymkhana",
		"Latitude": "18.92619766",
		"Longitude": "72.82672902",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 773,
		"Locality_Name": "National Gallery of Modern Art",
		"Latitude": "18.92591333",
		"Longitude": "72.83137008",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 774,
		"Locality_Name": "Cooperage Bandstand Garden",
		"Latitude": "18.92593842",
		"Longitude": "72.82826918",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 775,
		"Locality_Name": "Cooperage Football Ground",
		"Latitude": "18.92442457",
		"Longitude": "72.82867978",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 776,
		"Locality_Name": "Nariman Point (Sunset Point)",
		"Latitude": "18.92574324",
		"Longitude": "72.81859742",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 777,
		"Locality_Name": "Marine Drive, Madame Cama Road Junction",
		"Latitude": "18.92975718",
		"Longitude": "72.82160279",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 778,
		"Locality_Name": "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya",
		"Latitude": "18.92633136",
		"Longitude": "72.83159441",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 779,
		"Locality_Name": "BMC Pay & Park",
		"Latitude": "18.92475797",
		"Longitude": "72.82183102",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 780,
		"Locality_Name": "Shipping Corp Of India, Cityflo Stop",
		"Latitude": "18.92562893",
		"Longitude": "72.82587347",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 781,
		"Locality_Name": "N.C.P.A.",
		"Latitude": "18.92516078",
		"Longitude": "72.82261294",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 782,
		"Locality_Name": "Free Press Journal",
		"Latitude": "18.92296662",
		"Longitude": "72.82342406",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 783,
		"Locality_Name": "Indusind Bank, Cityflo Stop",
		"Latitude": "18.92498435",
		"Longitude": "72.82191755",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 784,
		"Locality_Name": "Bajaj Bhawan",
		"Latitude": "18.92650807",
		"Longitude": "72.82241363",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 785,
		"Locality_Name": "Cr 2 Mall, Cityflo Stop",
		"Latitude": "18.92619861",
		"Longitude": "72.82270078",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 786,
		"Locality_Name": "Free Press Marg",
		"Latitude": "18.92435594",
		"Longitude": "72.82491331",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 787,
		"Locality_Name": "Yashwantrao Chavan Pratishthan",
		"Latitude": "18.92560572",
		"Longitude": "72.82596976",
		"Station": {
			"id": 2
		}
	},
	{
		"id": 788,
		"Locality_Name": "Yogakshema Building",
		"Latitude": "18.92958562",
		"Longitude": "72.82395578",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 789,
		"Locality_Name": "Public Works Department",
		"Latitude": "18.93214035",
		"Longitude": "72.83068794",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 790,
		"Locality_Name": "High Court of Mumbai",
		"Latitude": "18.9313918",
		"Longitude": "72.83007396",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 791,
		"Locality_Name": "Mantralaya",
		"Latitude": "18.92703629",
		"Longitude": "72.82681134",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 792,
		"Locality_Name": "HR College",
		"Latitude": "18.92997853",
		"Longitude": "72.82662628",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 793,
		"Locality_Name": "KC College",
		"Latitude": "18.92977569",
		"Longitude": "72.82715898",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 794,
		"Locality_Name": "Jai Hind College",
		"Latitude": "18.93450481",
		"Longitude": "72.82522461",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 795,
		"Locality_Name": "Sydenham College of Commerce & Economics",
		"Latitude": "18.93525061",
		"Longitude": "72.82592291",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 796,
		"Locality_Name": "Government Law College",
		"Latitude": "18.93425507",
		"Longitude": "72.8269203",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 797,
		"Locality_Name": "Jamnalal Bajaj Institute",
		"Latitude": "18.92848532",
		"Longitude": "72.82741898",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 798,
		"Locality_Name": "University of Mumbai",
		"Latitude": "18.92935012",
		"Longitude": "72.82976591",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 799,
		"Locality_Name": "HPCL building",
		"Latitude": "18.92888819",
		"Longitude": "72.82518639",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 800,
		"Locality_Name": "Oval Maidan",
		"Latitude": "18.92967729",
		"Longitude": "72.82828126",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 801,
		"Locality_Name": "Jawaharlal Nehru Garden",
		"Latitude": "18.92862214",
		"Longitude": "72.82402457",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 802,
		"Locality_Name": "Mahatma Gandhi Garden",
		"Latitude": "18.92802165",
		"Longitude": "72.82475442",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 803,
		"Locality_Name": "Cross Maidan Garden",
		"Latitude": "18.93332808",
		"Longitude": "72.82879329",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 804,
		"Locality_Name": "Kasturi Building (The Hindu Newspaper Office)",
		"Latitude": "18.92974632",
		"Longitude": "72.8251161",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 805,
		"Locality_Name": "Cricket Club of India (CCI)",
		"Latitude": "18.93147006",
		"Longitude": "72.82451489",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 806,
		"Locality_Name": "CCI-Brabourne Stadium",
		"Latitude": "18.93326537",
		"Longitude": "72.82491144",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 807,
		"Locality_Name": "Wankhede Stadium (D-Road Entry)",
		"Latitude": "18.93688265",
		"Longitude": "72.8256738",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 808,
		"Locality_Name": "Mumbai Hockey Association Ground (D-Road Entry)",
		"Latitude": "18.93688265",
		"Longitude": "72.8256738",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 809,
		"Locality_Name": "Mumbai University Grounds (NSCB road entry)",
		"Latitude": "18.94053835",
		"Longitude": "72.8252828",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 810,
		"Locality_Name": "Marine Drive View Point (Near Air India)",
		"Latitude": "18.92977155",
		"Longitude": "72.82160349",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 811,
		"Locality_Name": "Western Railway Headquarters",
		"Latitude": "18.93366937",
		"Longitude": "72.82839458",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 812,
		"Locality_Name": "Churchgate Suburban Station (Western)",
		"Latitude": "18.93353224",
		"Longitude": "72.82775642",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 813,
		"Locality_Name": "Petroleum House",
		"Latitude": "18.9291159",
		"Longitude": "72.82505841",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 814,
		"Locality_Name": "Ahilyabai Holkar Chowk / Churchgate",
		"Latitude": "18.93211785",
		"Longitude": "72.8275992",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 815,
		"Locality_Name": "Churchgate Suburban Station",
		"Latitude": "18.93353224",
		"Longitude": "72.82775642",
		"Station": {
			"id": 3
		}
	},
	{
		"id": 816,
		"Locality_Name": "Oriental Building",
		"Latitude": "18.92491199",
		"Longitude": "72.83180309",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 817,
		"Locality_Name": "Sambava Chambers",
		"Latitude": "18.93430355",
		"Longitude": "72.83423589",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 818,
		"Locality_Name": "Reserve Bank Of India",
		"Latitude": "18.93318572",
		"Longitude": "72.8364577",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 819,
		"Locality_Name": "Government of Maharashtra bandhkam bhavan",
		"Latitude": "18.93723412",
		"Longitude": "72.83266516",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 820,
		"Locality_Name": "Central Bank of India",
		"Latitude": "18.93147187",
		"Longitude": "72.83216704",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 821,
		"Locality_Name": "STATE CET CELL",
		"Latitude": "18.9377269",
		"Longitude": "72.83308593",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 822,
		"Locality_Name": "Public Works Department (PWD)",
		"Latitude": "18.938345",
		"Longitude": "72.83297288",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 823,
		"Locality_Name": "Maharashtra Public Service Commission (MPSC)",
		"Latitude": "18.93092547",
		"Longitude": "72.83104057",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 824,
		"Locality_Name": "CE Office Jalsampada",
		"Latitude": "18.9316806",
		"Longitude": "72.83090293",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 825,
		"Locality_Name": "Special Court(TORTS)",
		"Latitude": "18.93115215",
		"Longitude": "72.83007957",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 826,
		"Locality_Name": "Hospital High Court",
		"Latitude": "18.93071938",
		"Longitude": "72.83056645",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 827,
		"Locality_Name": "High Court Pitch",
		"Latitude": "18.93156606",
		"Longitude": "72.82893534",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 828,
		"Locality_Name": "Directorate of Revenue Intelligence",
		"Latitude": "18.93786482",
		"Longitude": "72.82874231",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 829,
		"Locality_Name": "INS Angre",
		"Latitude": "18.93175205",
		"Longitude": "72.83729198",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 830,
		"Locality_Name": "Maharashtra State Womens Council",
		"Latitude": "18.93138195",
		"Longitude": "72.83573984",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 831,
		"Locality_Name": "Town Hall Post Office",
		"Latitude": "18.93107583",
		"Longitude": "72.83571367",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 832,
		"Locality_Name": "Office of District Collector",
		"Latitude": "18.93051121",
		"Longitude": "72.83587027",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 833,
		"Locality_Name": "Western Railway Headquarters",
		"Latitude": "18.93366937",
		"Longitude": "72.82839458",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 834,
		"Locality_Name": "Maharashtra State Legal Services Building",
		"Latitude": "18.93231729",
		"Longitude": "72.83023955",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 835,
		"Locality_Name": "The Bombay High Court",
		"Latitude": "18.93164518",
		"Longitude": "72.83000737",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 836,
		"Locality_Name": "Central Telegraph Office",
		"Latitude": "18.93287244",
		"Longitude": "72.83046046",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 837,
		"Locality_Name": "Lions Club of Bombay Host - Health Center",
		"Latitude": "18.93790474",
		"Longitude": "72.83350813",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 838,
		"Locality_Name": "Horniman Circle",
		"Latitude": "18.93203654",
		"Longitude": "72.83471905",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 839,
		"Locality_Name": "Taj Palace Hotel",
		"Latitude": "18.92220049",
		"Longitude": "72.83301176",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 840,
		"Locality_Name": "Anglo Scottish Educational Society",
		"Latitude": "18.93602626",
		"Longitude": "72.83254987",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 841,
		"Locality_Name": "Sir J J Fort Boys High School",
		"Latitude": "18.93688493",
		"Longitude": "72.8342857",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 842,
		"Locality_Name": "University of Mumbai",
		"Latitude": "18.92944726",
		"Longitude": "72.83094136",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 843,
		"Locality_Name": "K. R. Cama Oriental Institute",
		"Latitude": "18.9272332",
		"Longitude": "72.83367985",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 844,
		"Locality_Name": "Elphinstone College",
		"Latitude": "18.92718133",
		"Longitude": "72.83104575",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 845,
		"Locality_Name": "Sydenham College of Commerce & Economics",
		"Latitude": "18.93528822",
		"Longitude": "72.82592494",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 846,
		"Locality_Name": "State Central Library",
		"Latitude": "18.93183527",
		"Longitude": "72.83598201",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 847,
		"Locality_Name": "Siddharth College Of Law",
		"Latitude": "18.93411168",
		"Longitude": "72.83229347",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 848,
		"Locality_Name": "TCS house",
		"Latitude": "18.93794113",
		"Longitude": "72.83225893",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 849,
		"Locality_Name": "Bombay Stock Exchange (Bse)",
		"Latitude": "18.93003418",
		"Longitude": "72.83341903",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 850,
		"Locality_Name": "HSBC",
		"Latitude": "18.93119152",
		"Longitude": "72.83124843",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 851,
		"Locality_Name": "Standard Chartered Bank",
		"Latitude": "18.93361572",
		"Longitude": "72.8313877",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 852,
		"Locality_Name": "Tata Garden / Cross Maidan",
		"Latitude": "18.93436369",
		"Longitude": "72.82917752",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 853,
		"Locality_Name": "BMC Bhatia Udyan",
		"Latitude": "18.93864834",
		"Longitude": "72.83533154",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 854,
		"Locality_Name": "Cross Maidan",
		"Latitude": "18.93334784",
		"Longitude": "72.82922446",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 855,
		"Locality_Name": "St. Thomas Cathedral",
		"Latitude": "18.93216143",
		"Longitude": "72.83368685",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 856,
		"Locality_Name": "Bombay Gymkhana Squash Court",
		"Latitude": "18.9359436",
		"Longitude": "72.83201326",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 857,
		"Locality_Name": "Oval Maidan",
		"Latitude": "18.9297005",
		"Longitude": "72.82887774",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 858,
		"Locality_Name": "Azad Maidan",
		"Latitude": "18.93854918",
		"Longitude": "72.83231847",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 859,
		"Locality_Name": "Rbi Monetary Museum",
		"Latitude": "18.93385378",
		"Longitude": "72.83607481",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 860,
		"Locality_Name": "BSE bull statue",
		"Latitude": "18.93190424",
		"Longitude": "72.83413217",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 861,
		"Locality_Name": "Gate Way of India",
		"Latitude": "18.92198215",
		"Longitude": "72.83466182",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 862,
		"Locality_Name": "Jehangir Art Gallery",
		"Latitude": "18.92740928",
		"Longitude": "72.83163066",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 863,
		"Locality_Name": "Marine Drive View Point",
		"Latitude": "18.93181686",
		"Longitude": "72.82276511",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 864,
		"Locality_Name": "Flora Fountain",
		"Latitude": "18.93247732",
		"Longitude": "72.83147826",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 865,
		"Locality_Name": "Churchgate Suburban Railway Station (Western)",
		"Latitude": "18.93528184",
		"Longitude": "72.8271838",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 866,
		"Locality_Name": "Sidharth College / Hutatma Chowk",
		"Latitude": "18.93314596",
		"Longitude": "72.83187324",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 867,
		"Locality_Name": "Khadi Bhandar, Cityflo Stop",
		"Latitude": "18.93644861",
		"Longitude": "72.83387256",
		"Station": {
			"id": 4
		}
	},
	{
		"id": 868,
		"Locality_Name": "Handlooms House",
		"Latitude": "18.94762055",
		"Longitude": "72.83266114",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 869,
		"Locality_Name": "Mangaldas Market",
		"Latitude": "18.94865473",
		"Longitude": "72.83217367",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 870,
		"Locality_Name": "Alexandra Dock",
		"Latitude": "18.93353",
		"Longitude": "72.84225845",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 871,
		"Locality_Name": "Manish Market",
		"Latitude": "18.94666409",
		"Longitude": "72.83591337",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 872,
		"Locality_Name": "Crawford Market",
		"Latitude": "18.9476321",
		"Longitude": "72.83422934",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 873,
		"Locality_Name": "Indira Dock",
		"Latitude": "18.94160825",
		"Longitude": "72.84089009",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 874,
		"Locality_Name": "Brand Capital",
		"Latitude": "18.94155295",
		"Longitude": "72.83428377",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 875,
		"Locality_Name": "BMC Headquarter",
		"Latitude": "18.94043017",
		"Longitude": "72.83456761",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 876,
		"Locality_Name": "Metropolitan Court",
		"Latitude": "18.94159967",
		"Longitude": "72.83298994",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 877,
		"Locality_Name": "Azad Maidan Police Station",
		"Latitude": "18.94160132",
		"Longitude": "72.833152",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 878,
		"Locality_Name": "EOW offfice",
		"Latitude": "18.9462006",
		"Longitude": "72.83271522",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 879,
		"Locality_Name": "Small Causes Court",
		"Latitude": "18.94470936",
		"Longitude": "72.82994203",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 880,
		"Locality_Name": "Mtnl Fountain Teleohone Exchange",
		"Latitude": "18.93405479",
		"Longitude": "72.83063429",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 881,
		"Locality_Name": "Chief Metropolitan Magistrate Court",
		"Latitude": "18.94160914",
		"Longitude": "72.83278473",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 882,
		"Locality_Name": "Directorate of art, maharashtra",
		"Latitude": "18.94294377",
		"Longitude": "72.83346171",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 883,
		"Locality_Name": "Police Head Office",
		"Latitude": "18.945749",
		"Longitude": "72.83259087",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 884,
		"Locality_Name": "Office of the JT CP (Crime)",
		"Latitude": "18.94579211",
		"Longitude": "72.83326501",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 885,
		"Locality_Name": "Office of the commissioner of Police",
		"Latitude": "18.94609531",
		"Longitude": "72.83362421",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 886,
		"Locality_Name": "SB Office",
		"Latitude": "18.94439696",
		"Longitude": "72.8329215",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 887,
		"Locality_Name": "Foreigners Registration Office (FRRO)",
		"Latitude": "18.94452254",
		"Longitude": "72.83286094",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 888,
		"Locality_Name": "Directorate of Technical Education",
		"Latitude": "18.94383312",
		"Longitude": "72.83052074",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 889,
		"Locality_Name": "India Government Mint",
		"Latitude": "18.93368916",
		"Longitude": "72.8370738",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 890,
		"Locality_Name": "Docks Embarkation Hq",
		"Latitude": "18.94449096",
		"Longitude": "72.83973188",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 891,
		"Locality_Name": "Arogya Bhavan",
		"Latitude": "18.94337596",
		"Longitude": "72.83827483",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 892,
		"Locality_Name": "Central Railway Admin Building",
		"Latitude": "18.93993458",
		"Longitude": "72.83550481",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 893,
		"Locality_Name": "General Post Office",
		"Latitude": "18.94120888",
		"Longitude": "72.8372117",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 894,
		"Locality_Name": "The Cama & Albless Hospital",
		"Latitude": "18.94210288",
		"Longitude": "72.83223269",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 895,
		"Locality_Name": "Gokuldas Tejpal Hospital",
		"Latitude": "18.94496743",
		"Longitude": "72.83195303",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 896,
		"Locality_Name": "Saint George Hospital",
		"Latitude": "18.94067138",
		"Longitude": "72.83791788",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 897,
		"Locality_Name": "St.  Xavier's College",
		"Latitude": "18.94266959",
		"Longitude": "72.83152693",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 898,
		"Locality_Name": "Directorate of Technical Education/Elphinstone Technical Institute",
		"Latitude": "18.93524946",
		"Longitude": "72.83682761",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 899,
		"Locality_Name": "Government institute of printing technology",
		"Latitude": "18.94364604",
		"Longitude": "72.83421313",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 900,
		"Locality_Name": "Sydenham College of Commerce & Economics",
		"Latitude": "18.93536236",
		"Longitude": "72.82596377",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 901,
		"Locality_Name": "Government Dental College & Hospital Building",
		"Latitude": "18.93971922",
		"Longitude": "72.83779204",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 902,
		"Locality_Name": "Anjuman Islam School",
		"Latitude": "18.94282086",
		"Longitude": "72.8339903",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 903,
		"Locality_Name": "Sir JJ College of Arts & Architecture",
		"Latitude": "18.94514858",
		"Longitude": "72.83345106",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 904,
		"Locality_Name": "Times of India Building",
		"Latitude": "18.94136587",
		"Longitude": "72.83410024",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 905,
		"Locality_Name": "Sambava Chambers",
		"Latitude": "18.93436382",
		"Longitude": "72.83420586",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 906,
		"Locality_Name": "Britannia & Company",
		"Latitude": "18.93453536",
		"Longitude": "72.84029145",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 907,
		"Locality_Name": "Bmc Walter D,Souza Garden",
		"Latitude": "18.94252531",
		"Longitude": "72.82742709",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 908,
		"Locality_Name": "Tata Garden / Cross Maidan",
		"Latitude": "18.93437667",
		"Longitude": "72.82917162",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 909,
		"Locality_Name": "Rbi Monetary Museum",
		"Latitude": "18.93384808",
		"Longitude": "72.83604953",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 910,
		"Locality_Name": "The Press Club",
		"Latitude": "18.9408637",
		"Longitude": "72.83243288",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 911,
		"Locality_Name": "Wankhede Stadium (D-Road Entry)",
		"Latitude": "18.93828388",
		"Longitude": "72.82670786",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 912,
		"Locality_Name": "Bombay Gymkhana",
		"Latitude": "18.93727679",
		"Longitude": "72.83084888",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 913,
		"Locality_Name": "Churchgate Suburban Station",
		"Latitude": "18.93677957",
		"Longitude": "72.82720588",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 914,
		"Locality_Name": "CSMT Heritage",
		"Latitude": "18.94522567",
		"Longitude": "72.83938226",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 915,
		"Locality_Name": "CSMT Terminus",
		"Latitude": "18.94246004",
		"Longitude": "72.83676668",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 916,
		"Locality_Name": "CSMT Suburban Railway Station (Central & Harbor)",
		"Latitude": "18.93986042",
		"Longitude": "72.83538542",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 917,
		"Locality_Name": "Csmt (terminal)",
		"Latitude": "18.93986042",
		"Longitude": "72.83538542",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 918,
		"Locality_Name": "Mahapalika Marg, Dhobi Talao",
		"Latitude": "18.94271545",
		"Longitude": "72.83036605",
		"Station": {
			"id": 5
		}
	},
	{
		"id": 919,
		"Locality_Name": "Jer Mahal",
		"Latitude": "18.94389659",
		"Longitude": "72.82912071",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 920,
		"Locality_Name": "Swadeshi Market",
		"Latitude": "18.94951523",
		"Longitude": "72.82887001",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 921,
		"Locality_Name": "Mulji Jetha Market",
		"Latitude": "18.94894412",
		"Longitude": "72.83017412",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 922,
		"Locality_Name": "Manish Market",
		"Latitude": "18.94671157",
		"Longitude": "72.83534426",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 923,
		"Locality_Name": "Mumbai Market",
		"Latitude": "18.94622399",
		"Longitude": "72.82905401",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 924,
		"Locality_Name": "Javeri Bazaar",
		"Latitude": "18.94995532",
		"Longitude": "72.83037365",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 925,
		"Locality_Name": "Directorate of Technical Education",
		"Latitude": "18.94397507",
		"Longitude": "72.83034961",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 926,
		"Locality_Name": "Rang Bhavan",
		"Latitude": "18.94347824",
		"Longitude": "72.83136626",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 927,
		"Locality_Name": "Court of Small Cases",
		"Latitude": "18.94457522",
		"Longitude": "72.8299517",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 928,
		"Locality_Name": "Election Commission Nodal Office",
		"Latitude": "18.9431691",
		"Longitude": "72.82997731",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 929,
		"Locality_Name": "Maharashtra State Skills University (Mssu)",
		"Latitude": "18.94388623",
		"Longitude": "72.83011323",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 930,
		"Locality_Name": "St. Xavier's High School",
		"Latitude": "18.94399379",
		"Longitude": "72.83035895",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 931,
		"Locality_Name": "St. Xavier'S College",
		"Latitude": "18.94230806",
		"Longitude": "72.83127653",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 932,
		"Locality_Name": "Chandanwadi Crematorium",
		"Latitude": "18.94556362",
		"Longitude": "72.82509974",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 933,
		"Locality_Name": "Bada Khabristan",
		"Latitude": "18.94800523",
		"Longitude": "72.82254797",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 934,
		"Locality_Name": "Edward Cinema",
		"Latitude": "18.94513867",
		"Longitude": "72.82913829",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 935,
		"Locality_Name": "S.K Patil Gardens",
		"Latitude": "18.94990915",
		"Longitude": "72.82172172",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 936,
		"Locality_Name": "Walter D�Souza Garden",
		"Latitude": "18.94345597",
		"Longitude": "72.82772892",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 937,
		"Locality_Name": "Cowasji Jehangir Hall",
		"Latitude": "18.92561963",
		"Longitude": "72.8314675",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 938,
		"Locality_Name": "Metro Big Cinema",
		"Latitude": "18.94307747",
		"Longitude": "72.82917236",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 939,
		"Locality_Name": "BMC Walter D�souza Garden",
		"Latitude": "18.94268802",
		"Longitude": "72.82739647",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 940,
		"Locality_Name": "Marine Drive Beach",
		"Latitude": "18.94360051",
		"Longitude": "72.82286999",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 941,
		"Locality_Name": "S.K. Patil Garden",
		"Latitude": "18.94991518",
		"Longitude": "72.82173835",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 942,
		"Locality_Name": "Wadiaji Atash Behram (Parsi Agiary)",
		"Latitude": "18.94572505",
		"Longitude": "72.8272972",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 943,
		"Locality_Name": "Anjuman Atash Behram(Parsi Agiary)",
		"Latitude": "18.94534294",
		"Longitude": "72.82769959",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 944,
		"Locality_Name": "Kalbadevi Temple",
		"Latitude": "18.94852568",
		"Longitude": "72.82895402",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 945,
		"Locality_Name": "Bhatia Mahajan Wadi",
		"Latitude": "18.94805528",
		"Longitude": "72.82874827",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 946,
		"Locality_Name": "Dadiseth Ateshbehram",
		"Latitude": "18.95030726",
		"Longitude": "72.82680226",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 947,
		"Locality_Name": "St. Francis Xavier's Catholic Church",
		"Latitude": "18.94922147",
		"Longitude": "72.82332256",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 948,
		"Locality_Name": "Kyani & Co. Legendary Irani Restaurant, Bakers",
		"Latitude": "18.94405941",
		"Longitude": "72.82869457",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 949,
		"Locality_Name": "Mumbai Police Gymkhana",
		"Latitude": "18.94880625",
		"Longitude": "72.8201212",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 950,
		"Locality_Name": "Wilson Gymkhana",
		"Latitude": "18.94728671",
		"Longitude": "72.82124388",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 951,
		"Locality_Name": "Hindu Gymkhana",
		"Latitude": "18.94684599",
		"Longitude": "72.82156259",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 952,
		"Locality_Name": "Muslim Gymkhana",
		"Latitude": "18.94561527",
		"Longitude": "72.8235398",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 953,
		"Locality_Name": "Parsi Gymkhana",
		"Latitude": "18.94381166",
		"Longitude": "72.82344234",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 954,
		"Locality_Name": "Wankhede Stadium",
		"Latitude": "18.93843683",
		"Longitude": "72.8266787",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 955,
		"Locality_Name": "Girgaon Chowpatty Beach",
		"Latitude": "18.9553357",
		"Longitude": "72.81358995",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 956,
		"Locality_Name": "Lokmanya Bal Gangadhar Tilak Uddyan",
		"Latitude": "18.95498535",
		"Longitude": "72.81367962",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 957,
		"Locality_Name": "Marine Lines Suburban Railway Station (Western)",
		"Latitude": "18.94633634",
		"Longitude": "72.82363076",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 958,
		"Locality_Name": "Charni Road Suburban Railway Station (Western)",
		"Latitude": "18.9519086",
		"Longitude": "72.81850025",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 959,
		"Locality_Name": "Chandan Wadi / Princess Street",
		"Latitude": "18.94656287",
		"Longitude": "72.82710377",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 960,
		"Locality_Name": "Kalba Devi",
		"Latitude": "18.94721087",
		"Longitude": "72.82871803",
		"Station": {
			"id": 6
		}
	},
	{
		"id": 961,
		"Locality_Name": "Saifee Hospital",
		"Latitude": "18.95242593",
		"Longitude": "72.81811901",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 962,
		"Locality_Name": "Mackichan Hall",
		"Latitude": "18.95669339",
		"Longitude": "72.81014621",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 963,
		"Locality_Name": "Wilson College",
		"Latitude": "18.95615826",
		"Longitude": "72.81081919",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 964,
		"Locality_Name": "Bharati Vidya Bhavan",
		"Latitude": "18.95734783",
		"Longitude": "72.8105783",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 965,
		"Locality_Name": "The Royal Opera House",
		"Latitude": "18.95592952",
		"Longitude": "72.81566264",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 966,
		"Locality_Name": "S.K. Patil Garden",
		"Latitude": "18.94990092",
		"Longitude": "72.82173541",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 967,
		"Locality_Name": "Sri Venkateswara Balaji Mandir (Fanaswadi)",
		"Latitude": "18.95188597",
		"Longitude": "72.82560065",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 968,
		"Locality_Name": "Parsi Agiary",
		"Latitude": "18.95043954",
		"Longitude": "72.82692025",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 969,
		"Locality_Name": "Kalaram Mandir",
		"Latitude": "18.95151459",
		"Longitude": "72.82303167",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 970,
		"Locality_Name": "Taraporevala Aquarium",
		"Latitude": "18.94919427",
		"Longitude": "72.81981873",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 971,
		"Locality_Name": "Charni Road Suburban Railway Station (Western)",
		"Latitude": "18.95191403",
		"Longitude": "72.81849512",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 972,
		"Locality_Name": "Charni road train station",
		"Latitude": "18.95191403",
		"Longitude": "72.81849512",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 973,
		"Locality_Name": "Thakurdwar",
		"Latitude": "18.95210442",
		"Longitude": "72.82333835",
		"Station": {
			"id": 7
		}
	},
	{
		"id": 974,
		"Locality_Name": "Nana Chowk",
		"Latitude": "18.9615719",
		"Longitude": "72.81318737",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 975,
		"Locality_Name": "Sir H. N. Reliance Foundation  Hospital And Research Centre",
		"Latitude": "18.95885119",
		"Longitude": "72.81978639",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 976,
		"Locality_Name": "Mackichan Hall",
		"Latitude": "18.95669299",
		"Longitude": "72.81013964",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 977,
		"Locality_Name": "Wilson College",
		"Latitude": "18.9562744",
		"Longitude": "72.81088215",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 978,
		"Locality_Name": "Nana Nani Park",
		"Latitude": "18.95575827",
		"Longitude": "72.8098123",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 979,
		"Locality_Name": "Bharati Vidya Bhavan",
		"Latitude": "18.95732651",
		"Longitude": "72.81052816",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 980,
		"Locality_Name": "Kamla Nehru Park",
		"Latitude": "18.9549539",
		"Longitude": "72.80518401",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 981,
		"Locality_Name": "Royal Opera House",
		"Latitude": "18.95598002",
		"Longitude": "72.81589854",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 982,
		"Locality_Name": "Mahanagar Pallika Park",
		"Latitude": "18.96482593",
		"Longitude": "72.82002425",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 983,
		"Locality_Name": "Hanging Gardens",
		"Latitude": "18.95702477",
		"Longitude": "72.80590204",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 984,
		"Locality_Name": "Babulnath Temple",
		"Latitude": "18.95734026",
		"Longitude": "72.80849022",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 985,
		"Locality_Name": "Iskon Temple",
		"Latitude": "18.95762995",
		"Longitude": "72.8098081",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 986,
		"Locality_Name": "Mahella Patel Agiary",
		"Latitude": "18.96271955",
		"Longitude": "72.81911539",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 987,
		"Locality_Name": "August Kranti Maidan",
		"Latitude": "18.96279769",
		"Longitude": "72.81034034",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 988,
		"Locality_Name": "Mani Bhavan",
		"Latitude": "18.95978049",
		"Longitude": "72.81147505",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 989,
		"Locality_Name": "Grant Road Suburban Railway Station (Western)",
		"Latitude": "18.96318141",
		"Longitude": "72.81639888",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 990,
		"Locality_Name": "Jio-Bp Pulse Charging Station",
		"Latitude": "18.96459483",
		"Longitude": "72.82129091",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 991,
		"Locality_Name": "Minerva Cinema",
		"Latitude": "18.96389242",
		"Longitude": "72.81852145",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 992,
		"Locality_Name": "Dr .Bhadkamkar Road Junction / Novelty",
		"Latitude": "18.96198632",
		"Longitude": "72.81874087",
		"Station": {
			"id": 8
		}
	},
	{
		"id": 993,
		"Locality_Name": "Reserve Bank of India",
		"Latitude": "18.97015767",
		"Longitude": "72.82149996",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 994,
		"Locality_Name": "Tardeo RTO",
		"Latitude": "18.97331658",
		"Longitude": "72.81668013",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 995,
		"Locality_Name": "Consulate General Of Indonesia",
		"Latitude": "18.96559864",
		"Longitude": "72.80935119",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 996,
		"Locality_Name": "Consulate General Of Italy",
		"Latitude": "18.96430926",
		"Longitude": "72.80741968",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 997,
		"Locality_Name": "Central Drugs Standard Control",
		"Latitude": "18.96678844",
		"Longitude": "72.82299036",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 998,
		"Locality_Name": "Consulate General Of Japan",
		"Latitude": "18.97526669",
		"Longitude": "72.81091886",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 999,
		"Locality_Name": "Jaslok Hospital",
		"Latitude": "18.97149781",
		"Longitude": "72.8096042",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1000,
		"Locality_Name": "Breach Candy Hospital",
		"Latitude": "18.97257524",
		"Longitude": "72.80465252",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1001,
		"Locality_Name": "B D Petit Parsee Hospital",
		"Latitude": "18.9688625",
		"Longitude": "72.8057139",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1002,
		"Locality_Name": "Nair Hospital",
		"Latitude": "18.9729197",
		"Longitude": "72.82183899",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1003,
		"Locality_Name": "Wockhardt Hospital",
		"Latitude": "18.97542716",
		"Longitude": "72.82372761",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1004,
		"Locality_Name": "Maratha Mandir's Babasaheb Gawde Institute Of Technology",
		"Latitude": "18.97079004",
		"Longitude": "72.82175871",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1005,
		"Locality_Name": "Sophia Centre For Women'S Studies And Development",
		"Latitude": "18.96921791",
		"Longitude": "72.80801921",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1006,
		"Locality_Name": "Industrial Training Institute",
		"Latitude": "18.97679342",
		"Longitude": "72.82286524",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1007,
		"Locality_Name": "Maratha Mandir",
		"Latitude": "18.97147496",
		"Longitude": "72.82202355",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1008,
		"Locality_Name": "Shree Mahalakshmi Temple",
		"Latitude": "18.97745804",
		"Longitude": "72.80667477",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1009,
		"Locality_Name": "Mahella Patel Agiary",
		"Latitude": "18.9627259",
		"Longitude": "72.81912274",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1010,
		"Locality_Name": "Imperial Towers",
		"Latitude": "18.97070664",
		"Longitude": "72.81292086",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1011,
		"Locality_Name": "Willingdon Sports Club",
		"Latitude": "18.97659503",
		"Longitude": "72.81532778",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1012,
		"Locality_Name": "National Museum of Indian Cinema",
		"Latitude": "18.97049708",
		"Longitude": "72.8088743",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1013,
		"Locality_Name": "National Museum Of Indian Cinema",
		"Latitude": "18.97047392",
		"Longitude": "72.80889975",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1014,
		"Locality_Name": "Msrtc Intercity Bus Depot",
		"Latitude": "18.96892479",
		"Longitude": "72.82185325",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1015,
		"Locality_Name": "BEST Bus Depot",
		"Latitude": "18.96898376",
		"Longitude": "72.82425458",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1016,
		"Locality_Name": "Jio-Bp Pulse Charging Station",
		"Latitude": "18.96458592",
		"Longitude": "72.82130419",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1017,
		"Locality_Name": "Mumbai Central Railway Station",
		"Latitude": "18.9707195",
		"Longitude": "72.81994753",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1018,
		"Locality_Name": "Mumbai Central",
		"Latitude": "18.97023392",
		"Longitude": "72.82125873",
		"Station": {
			"id": 9
		}
	},
	{
		"id": 1019,
		"Locality_Name": "Dhobi Ghat",
		"Latitude": "18.98225785",
		"Longitude": "72.82552375",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1020,
		"Locality_Name": "Arthur Road Central Jail",
		"Latitude": "18.98473645",
		"Longitude": "72.82992027",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1021,
		"Locality_Name": "Kasturba Hospital",
		"Latitude": "18.98420634",
		"Longitude": "72.82968503",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1022,
		"Locality_Name": "All India Institute Of Physical Medicine And Rehabilitation",
		"Latitude": "18.97857519",
		"Longitude": "72.81326888",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1023,
		"Locality_Name": "St. Ignatius Church",
		"Latitude": "18.98270967",
		"Longitude": "72.82833927",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1024,
		"Locality_Name": "Haji Ali Darga",
		"Latitude": "18.98267213",
		"Longitude": "72.80880698",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1025,
		"Locality_Name": "Essar House",
		"Latitude": "18.97903728",
		"Longitude": "72.81972176",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1026,
		"Locality_Name": "National Sports Club Of India",
		"Latitude": "18.98506149",
		"Longitude": "72.81524293",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1027,
		"Locality_Name": "Mahalakshmi Race Cource",
		"Latitude": "18.98419274",
		"Longitude": "72.82003501",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1028,
		"Locality_Name": "Nehuru Science Centre",
		"Latitude": "18.99181538",
		"Longitude": "72.82072006",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1029,
		"Locality_Name": "Mahalakshmi Suburban Railway Station (Western)",
		"Latitude": "18.9753132",
		"Longitude": "72.82169549",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1030,
		"Locality_Name": "Sant Gadge Maharaj Chowk monorail",
		"Latitude": "18.98320955",
		"Longitude": "72.8287494",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1031,
		"Locality_Name": "Mahalakshmi Train Station",
		"Latitude": "18.9753132",
		"Longitude": "72.82169549",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1032,
		"Locality_Name": "Satrasta, RTO Colony",
		"Latitude": "18.98068852",
		"Longitude": "72.82644146",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1033,
		"Locality_Name": "Sant Gadge Maharaj Chowk",
		"Latitude": "18.98109481",
		"Longitude": "72.82729793",
		"Station": {
			"id": 10
		}
	},
	{
		"id": 1034,
		"Locality_Name": "High Street Phoenix Mall",
		"Latitude": "18.9948619",
		"Longitude": "72.8256677",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1035,
		"Locality_Name": "Love Grove Waste Water Treatment Plant",
		"Latitude": "18.99216421",
		"Longitude": "72.81542852",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1036,
		"Locality_Name": "World One The Word Towers",
		"Latitude": "19.00203173",
		"Longitude": "72.82658398",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1037,
		"Locality_Name": "Peninsula Corporate Park",
		"Latitude": "18.99877083",
		"Longitude": "72.82572116",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1038,
		"Locality_Name": "The National Sports Club Of India",
		"Latitude": "18.98607279",
		"Longitude": "72.81456849",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1039,
		"Locality_Name": "Nehru Planetarium",
		"Latitude": "18.98977227",
		"Longitude": "72.81481579",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1040,
		"Locality_Name": "Nehru Centre Art Gallery",
		"Latitude": "18.98866424",
		"Longitude": "72.81471686",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1041,
		"Locality_Name": "Lower Parel Suburban Railway Station (Western)",
		"Latitude": "18.99680046",
		"Longitude": "72.82980984",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1042,
		"Locality_Name": "Lower parel train station",
		"Latitude": "18.99680046",
		"Longitude": "72.82980984",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1043,
		"Locality_Name": "Famous Studios.",
		"Latitude": "18.98938108",
		"Longitude": "72.82281958",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1044,
		"Locality_Name": "Haji Usman Seth Rakhangi Chowk",
		"Latitude": "18.98959654",
		"Longitude": "72.82313004",
		"Station": {
			"id": 11
		}
	},
	{
		"id": 1045,
		"Locality_Name": "Atria Mall",
		"Latitude": "18.99126333",
		"Longitude": "72.81421274",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1046,
		"Locality_Name": "MCGM Engineering Hub",
		"Latitude": "18.99553103",
		"Longitude": "72.81834683",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1047,
		"Locality_Name": "RTO - RegionalTransport Office, Worli",
		"Latitude": "19.01307156",
		"Longitude": "72.81819875",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1048,
		"Locality_Name": "Dairy Development Department",
		"Latitude": "18.9976259",
		"Longitude": "72.81192589",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1049,
		"Locality_Name": "Consulate General Of The Republic Of Korea (South Korea)",
		"Latitude": "18.99767597",
		"Longitude": "72.81798137",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1050,
		"Locality_Name": "Anti-Corruption Bureau",
		"Latitude": "19.00636606",
		"Longitude": "72.81650811",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1051,
		"Locality_Name": "Employees State Insurance Corporation",
		"Latitude": "19.00181896",
		"Longitude": "72.8168916",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1052,
		"Locality_Name": "Podar Medical College And Hospital",
		"Latitude": "19.0026148",
		"Longitude": "72.81584815",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1053,
		"Locality_Name": "Ambe Internationa Humane",
		"Latitude": "18.9960994",
		"Longitude": "72.81919367",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1054,
		"Locality_Name": "Adya Shankaracharya Garden",
		"Latitude": "19.00781549",
		"Longitude": "72.81644603",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1055,
		"Locality_Name": "Nehru Planetarium",
		"Latitude": "18.98979478",
		"Longitude": "72.81485098",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1056,
		"Locality_Name": "Nehru Science Centre",
		"Latitude": "18.99176933",
		"Longitude": "72.82089556",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1057,
		"Locality_Name": "Nehru Centre",
		"Latitude": "18.99179261",
		"Longitude": "72.82085346",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1058,
		"Locality_Name": "Jio-Bp Plus Charging Station",
		"Latitude": "18.98680851",
		"Longitude": "72.81428896",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1059,
		"Locality_Name": "Acharya Atre Chowk",
		"Latitude": "18.99866106",
		"Longitude": "72.81789209",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1060,
		"Locality_Name": "Worli Naka, Cityflo Stop - Bus stop",
		"Latitude": "18.99998109",
		"Longitude": "72.81790129",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1061,
		"Locality_Name": "Mahanagar Palika Yangraha - Bus stop",
		"Latitude": "18.99550341",
		"Longitude": "72.81914306",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1062,
		"Locality_Name": "Jijamata Nagar - Bus stop",
		"Latitude": "18.99324956",
		"Longitude": "72.8201462",
		"Station": {
			"id": 12
		}
	},
	{
		"id": 1063,
		"Locality_Name": "Kamala Mills Compound",
		"Latitude": "19.00295973",
		"Longitude": "72.82867128",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1064,
		"Locality_Name": "One Worldcentre",
		"Latitude": "19.00710398",
		"Longitude": "72.83333111",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1065,
		"Locality_Name": "Doordarshan Sahyadri",
		"Latitude": "19.00665373",
		"Longitude": "72.82106217",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1066,
		"Locality_Name": "Worli Police Station",
		"Latitude": "19.00523476",
		"Longitude": "72.81742061",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1067,
		"Locality_Name": "MCGM Office",
		"Latitude": "19.0037297",
		"Longitude": "72.81782264",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1068,
		"Locality_Name": "Regional Passport Office, Mumbai",
		"Latitude": "19.01131054",
		"Longitude": "72.8210918",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1069,
		"Locality_Name": "Worli Fire Station",
		"Latitude": "19.0137539",
		"Longitude": "72.82343379",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1070,
		"Locality_Name": "Mumbai Traffic Police H",
		"Latitude": "19.01011207",
		"Longitude": "72.81771441",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1071,
		"Locality_Name": "Maharashtra State Police Housing & Welfare Corporation Ltd",
		"Latitude": "19.00908483",
		"Longitude": "72.81714415",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1072,
		"Locality_Name": "Maharashtra Rifle Association",
		"Latitude": "19.01542368",
		"Longitude": "72.81749613",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1073,
		"Locality_Name": "New Charity Commissioner Office",
		"Latitude": "19.01034976",
		"Longitude": "72.8198417",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1074,
		"Locality_Name": "Indian Coast Guard Rhq (West)",
		"Latitude": "19.01729533",
		"Longitude": "72.81728875",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1075,
		"Locality_Name": "Doordarshan Kendra Worli",
		"Latitude": "19.00653463",
		"Longitude": "72.82017508",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1076,
		"Locality_Name": "Anti-Corruption Bureau",
		"Latitude": "19.00676839",
		"Longitude": "72.81626323",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1077,
		"Locality_Name": "Indian Navy Administrative Building",
		"Latitude": "19.01558293",
		"Longitude": "72.81665706",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1078,
		"Locality_Name": "People�S Mobile Hospital",
		"Latitude": "19.0066212",
		"Longitude": "72.81791286",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1079,
		"Locality_Name": "Worli Hospital For Women",
		"Latitude": "19.01334118",
		"Longitude": "72.82261414",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1080,
		"Locality_Name": "Podar Medical College And Hospital",
		"Latitude": "19.00270545",
		"Longitude": "72.81590525",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1081,
		"Locality_Name": "Bosco Ent Nursing Home",
		"Latitude": "19.00611517",
		"Longitude": "72.81825967",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1082,
		"Locality_Name": "Glaxo Smith Kline",
		"Latitude": "19.00887098",
		"Longitude": "72.81981289",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1083,
		"Locality_Name": "Sasmira Institute Of Management Studies",
		"Latitude": "19.0106264",
		"Longitude": "72.81987238",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1084,
		"Locality_Name": "Watumull Institute",
		"Latitude": "19.00352604",
		"Longitude": "72.81367624",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1085,
		"Locality_Name": "Pandurang Budhakar Marg",
		"Latitude": "19.00643867",
		"Longitude": "72.82450611",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1086,
		"Locality_Name": "Aditya Birla Center",
		"Latitude": "19.01097801",
		"Longitude": "72.8220705",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1087,
		"Locality_Name": "Mahindra Tower",
		"Latitude": "19.00577843",
		"Longitude": "72.82186846",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1088,
		"Locality_Name": "Bengal Chemicals & Pharmaceuticals Ltd",
		"Latitude": "19.01417666",
		"Longitude": "72.82453661",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1089,
		"Locality_Name": "Birla Aurora",
		"Latitude": "19.01245842",
		"Longitude": "72.82330654",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1090,
		"Locality_Name": "Lion Garden",
		"Latitude": "19.01049909",
		"Longitude": "72.81886142",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1091,
		"Locality_Name": "Worli Police Camp Ground",
		"Latitude": "19.00873448",
		"Longitude": "72.81586935",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1092,
		"Locality_Name": "Adya Shankaracharya Garden",
		"Latitude": "19.00795231",
		"Longitude": "72.81655001",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1093,
		"Locality_Name": "Bhagwan Gautam Budha Udhyan",
		"Latitude": "19.00868364",
		"Longitude": "72.81509535",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1094,
		"Locality_Name": "Worli Sea Face Garden",
		"Latitude": "19.01484599",
		"Longitude": "72.8167022",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1095,
		"Locality_Name": "Nipponzan Myohoji Budha Temple",
		"Latitude": "19.00109765",
		"Longitude": "72.81603697",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1096,
		"Locality_Name": "Koliwada",
		"Latitude": "19.01869099",
		"Longitude": "72.8176479",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1097,
		"Locality_Name": "Oberoi 360 West",
		"Latitude": "19.01139324",
		"Longitude": "72.8232985",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1098,
		"Locality_Name": "Lodha World One",
		"Latitude": "19.00295147",
		"Longitude": "72.82651305",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1099,
		"Locality_Name": "Worli Fort",
		"Latitude": "19.02464219",
		"Longitude": "72.81657265",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1100,
		"Locality_Name": "Worli Koliwada Jetty",
		"Latitude": "19.02639897",
		"Longitude": "72.81550926",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1101,
		"Locality_Name": "Cleveland Bunder",
		"Latitude": "19.01662371",
		"Longitude": "72.81747516",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1102,
		"Locality_Name": "Dr. Ravindra Kulkarni Chowk",
		"Latitude": "19.0103329",
		"Longitude": "72.82050317",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1103,
		"Locality_Name": "Babasaheb Worlikar Chowk - Bus stop",
		"Latitude": "19.01244973",
		"Longitude": "72.82222686",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1104,
		"Locality_Name": "Doordarshan - Bus stop",
		"Latitude": "19.00718926",
		"Longitude": "72.81865524",
		"Station": {
			"id": 13
		}
	},
	{
		"id": 1105,
		"Locality_Name": "Car Trade",
		"Latitude": "19.01307929",
		"Longitude": "72.82657623",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1106,
		"Locality_Name": "Vijay Sales Electronics Shopping Mall",
		"Latitude": "19.01812129",
		"Longitude": "72.83054907",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1107,
		"Locality_Name": "Appasaheb Marathe Marg- Car Showrooms & Commercial Zone",
		"Latitude": "19.0130732",
		"Longitude": "72.82650771",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1108,
		"Locality_Name": "Wadia International Center",
		"Latitude": "19.00731275",
		"Longitude": "72.82924838",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1109,
		"Locality_Name": "Textile Committee Of India",
		"Latitude": "19.01707756",
		"Longitude": "72.82693331",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1110,
		"Locality_Name": "MTNL, Prabhadevi Telecom Bldg",
		"Latitude": "19.02169896",
		"Longitude": "72.8341198",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1111,
		"Locality_Name": "Registration Office",
		"Latitude": "19.01639062",
		"Longitude": "72.82423162",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1112,
		"Locality_Name": "Kabootar Khana Circle",
		"Latitude": "19.01896279",
		"Longitude": "72.84044415",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1113,
		"Locality_Name": "Hotel Kohinoor Park",
		"Latitude": "19.0167915",
		"Longitude": "72.82914859",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1114,
		"Locality_Name": "Marathe Udyog Bhavan",
		"Latitude": "19.01301083",
		"Longitude": "72.82840676",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1115,
		"Locality_Name": "Rachana Sansad'S Academy Of Architecture",
		"Latitude": "19.0150272",
		"Longitude": "72.83125269",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1116,
		"Locality_Name": "Convent Girls High School",
		"Latitude": "19.01646704",
		"Longitude": "72.83174117",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1117,
		"Locality_Name": "Municipal School",
		"Latitude": "19.0165963",
		"Longitude": "72.83479862",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1118,
		"Locality_Name": "Adv. Balasaheb Apte College Of Law",
		"Latitude": "19.01712119",
		"Longitude": "72.83440122",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1119,
		"Locality_Name": "Maharashtra High School Number 2",
		"Latitude": "19.01714065",
		"Longitude": "72.83435927",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1120,
		"Locality_Name": "Our Lady Of Salvation High School",
		"Latitude": "19.01813462",
		"Longitude": "72.83513195",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1121,
		"Locality_Name": "Nabar Guruji School",
		"Latitude": "19.01971532",
		"Longitude": "72.83685599",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1122,
		"Locality_Name": "National Skill Training Institute For Women (Nsti)",
		"Latitude": "19.01957925",
		"Longitude": "72.83244502",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1123,
		"Locality_Name": "Kirti M.  Doongursee College Of Arts,Science & Commerce",
		"Latitude": "19.02096822",
		"Longitude": "72.83114019",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1124,
		"Locality_Name": "ITI Dadar",
		"Latitude": "19.01933308",
		"Longitude": "72.83237121",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1125,
		"Locality_Name": "The Stephen High School For The Deaf And Aphasic",
		"Latitude": "19.01690839",
		"Longitude": "72.83168155",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1126,
		"Locality_Name": "Shardashram Vidyamandir International School",
		"Latitude": "19.01541986",
		"Longitude": "72.83722965",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1127,
		"Locality_Name": "Prabhadevi Beach",
		"Latitude": "19.01815128",
		"Longitude": "72.824919",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1128,
		"Locality_Name": "Dadar Beach",
		"Latitude": "19.02091207",
		"Longitude": "72.82927538",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1129,
		"Locality_Name": "Prabhadevi Beach",
		"Latitude": "19.01828367",
		"Longitude": "72.82487715",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1130,
		"Locality_Name": "Sane Guruji Garden",
		"Latitude": "19.01645534",
		"Longitude": "72.82994443",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1131,
		"Locality_Name": "Nardulla Tank Maidan",
		"Latitude": "19.01590659",
		"Longitude": "72.83102715",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1132,
		"Locality_Name": "Ravindra Natya Mandir",
		"Latitude": "19.01534972",
		"Longitude": "72.83062657",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1133,
		"Locality_Name": "P L.  Deshpande Maharashtra Kala Academy",
		"Latitude": "19.01518228",
		"Longitude": "72.83059352",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1134,
		"Locality_Name": "Maharashtra State Sahitya Ani Sanskriti Mandal",
		"Latitude": "19.01551315",
		"Longitude": "72.83036058",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1135,
		"Locality_Name": "Prabhadevi Ground",
		"Latitude": "19.01350024",
		"Longitude": "72.8267706",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1136,
		"Locality_Name": "Shree Siddhivinayak Ganpati Mandir",
		"Latitude": "19.01704806",
		"Longitude": "72.83039162",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1137,
		"Locality_Name": "Prabhadevi Mandir",
		"Latitude": "19.01430903",
		"Longitude": "72.82743204",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1138,
		"Locality_Name": "Our Lady Of Salvation Church",
		"Latitude": "19.01896151",
		"Longitude": "72.83623996",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1139,
		"Locality_Name": "Worli Sports Club",
		"Latitude": "19.01473118",
		"Longitude": "72.8219249",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1140,
		"Locality_Name": "Ravindra Natya Mandir",
		"Latitude": "19.01470908",
		"Longitude": "72.83034623",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1141,
		"Locality_Name": "Siddhivinayak Mandir",
		"Latitude": "19.01489658",
		"Longitude": "72.83175078",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1142,
		"Locality_Name": "Prabhadevi / Siddhivinayak",
		"Latitude": "19.01580761",
		"Longitude": "72.8278521",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1143,
		"Locality_Name": "Gammon House - Bus stop",
		"Latitude": "19.01467868",
		"Longitude": "72.82623108",
		"Station": {
			"id": 14
		}
	},
	{
		"id": 1144,
		"Locality_Name": "Kohinoor Square",
		"Latitude": "19.02501118",
		"Longitude": "72.84151384",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1145,
		"Locality_Name": "Dadar Shopping Centre",
		"Latitude": "19.02002544",
		"Longitude": "72.8413672",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1146,
		"Locality_Name": "Gold Market Lane Ranade Road",
		"Latitude": "19.01885047",
		"Longitude": "72.84104183",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1147,
		"Locality_Name": "CCIL Bhavan",
		"Latitude": "19.01955124",
		"Longitude": "72.83495907",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1148,
		"Locality_Name": "Shushrusha Hospital",
		"Latitude": "19.02348046",
		"Longitude": "72.83775694",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1149,
		"Locality_Name": "Kabootar Khana Circle",
		"Latitude": "19.01928635",
		"Longitude": "72.84036658",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1150,
		"Locality_Name": "Balmohan Vidyamandir",
		"Latitude": "19.02535265",
		"Longitude": "72.83922367",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1151,
		"Locality_Name": "Institute Of Hotel Management, Catering Technology And Applied Nutrition",
		"Latitude": "19.02362009",
		"Longitude": "72.83493003",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1152,
		"Locality_Name": "Kohinoor Catering College",
		"Latitude": "19.02278825",
		"Longitude": "72.83597643",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1153,
		"Locality_Name": "Dr.  Antonio Da Silva High School & Jr College",
		"Latitude": "19.02025808",
		"Longitude": "72.84008621",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1154,
		"Locality_Name": "D. G.  Ruparel College Of Arts, Science & Commerce",
		"Latitude": "19.02806457",
		"Longitude": "72.84531979",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1155,
		"Locality_Name": "Kirti M. Doongursee College Of Arts, Science And Commerce",
		"Latitude": "19.02146858",
		"Longitude": "72.83103883",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1156,
		"Locality_Name": "Dadar Chowpatty",
		"Latitude": "19.02688913",
		"Longitude": "72.83453979",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1157,
		"Locality_Name": "Balasaheb Thakeray Memorial",
		"Latitude": "19.02724731",
		"Longitude": "72.83706945",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1158,
		"Locality_Name": "Shiv Sena Headquarters",
		"Latitude": "19.02461282",
		"Longitude": "72.84050074",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1159,
		"Locality_Name": "Yashwant Rao Chavan Auditorium",
		"Latitude": "19.02710824",
		"Longitude": "72.84327499",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1160,
		"Locality_Name": "Swatantryaveer Savarkar Rashtriya Smarak",
		"Latitude": "19.02844255",
		"Longitude": "72.83696818",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1161,
		"Locality_Name": "Samyukta Maharashtra Smruti Dalan",
		"Latitude": "19.02803856",
		"Longitude": "72.83671059",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1162,
		"Locality_Name": "Vanita Samaj",
		"Latitude": "19.02757229",
		"Longitude": "72.8361757",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1163,
		"Locality_Name": "Cinema Plaza",
		"Latitude": "19.02206986",
		"Longitude": "72.84272221",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1164,
		"Locality_Name": "Shivaji Mandir",
		"Latitude": "19.02276265",
		"Longitude": "72.84224919",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1166,
		"Locality_Name": "Shivaji Park",
		"Latitude": "19.02689544",
		"Longitude": "72.83820162",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1167,
		"Locality_Name": "Portuguese Church",
		"Latitude": "19.01891644",
		"Longitude": "72.83617881",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1168,
		"Locality_Name": "Shri Mahaveer Digambar Jain Mandir",
		"Latitude": "19.02398067",
		"Longitude": "72.84197517",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1169,
		"Locality_Name": "Dr. B R Ambedkar Chaitya Bhoomi",
		"Latitude": "19.02630764",
		"Longitude": "72.83457885",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1170,
		"Locality_Name": "Mayor�S Bungalow",
		"Latitude": "19.02919253",
		"Longitude": "72.83660207",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1171,
		"Locality_Name": "Gypsy Chinese",
		"Latitude": "19.02524591",
		"Longitude": "72.84005482",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1172,
		"Locality_Name": "Mahatma Gandhi Memorial Swimming Pool",
		"Latitude": "19.02805522",
		"Longitude": "72.83665372",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1173,
		"Locality_Name": "Shivaji Park Gymkhana",
		"Latitude": "19.02585939",
		"Longitude": "72.83872055",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1174,
		"Locality_Name": "Maharashtra State Kabbadi Association",
		"Latitude": "19.02665959",
		"Longitude": "72.83683135",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1175,
		"Locality_Name": "Dadar Railway Station (Western & Central) Suburban & Long Distance",
		"Latitude": "19.01956703",
		"Longitude": "72.8429389",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1176,
		"Locality_Name": "Matunga Road Suburban Railway Station (Western)",
		"Latitude": "19.02887484",
		"Longitude": "72.84698442",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1177,
		"Locality_Name": "Dadar Railway Station & Market",
		"Latitude": "19.01956703",
		"Longitude": "72.8429389",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1178,
		"Locality_Name": "Matunga Road Railway Station",
		"Latitude": "19.02887484",
		"Longitude": "72.84698442",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1179,
		"Locality_Name": "Ranade Road Junction - Bus Stop",
		"Latitude": "19.02208678",
		"Longitude": "72.83775586",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1180,
		"Locality_Name": "Ranade Road Junction - Bus Stop",
		"Latitude": "19.02156342",
		"Longitude": "72.83761831",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1181,
		"Locality_Name": "Shivaji Park/Ram Ganesh Gadkari Chowk - Bus Stop",
		"Latitude": "19.02598813",
		"Longitude": "72.84077141",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1182,
		"Locality_Name": "Shivaji Park/Ram Ganesh Gadkari Chowk - Bus Stop",
		"Latitude": "19.02582361",
		"Longitude": "72.84095418",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1183,
		"Locality_Name": "Shivaji Park/Ram Ganesh Gadkari Chowk - Bus Stop",
		"Latitude": "19.02642254",
		"Longitude": "72.8410686",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1184,
		"Locality_Name": "Shivaji Park/Ram Ganesh Gadkari Chowk - Bus Stop",
		"Latitude": "19.02663638",
		"Longitude": "72.84093071",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1185,
		"Locality_Name": "Shivaji Park/Ram Ganesh Gadkari Chowk - Bus Stop",
		"Latitude": "19.02397171",
		"Longitude": "72.84128938",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1186,
		"Locality_Name": "Shivaji Mandir",
		"Latitude": "19.02340498",
		"Longitude": "72.84166638",
		"Station": {
			"id": 15
		}
	},
	{
		"id": 1187,
		"Locality_Name": "P. D.  Hinduja Hospital & Medical Research Centre",
		"Latitude": "19.03329943",
		"Longitude": "72.83911129",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1188,
		"Locality_Name": "Hinduja Hospital Opd Building",
		"Latitude": "19.06841966",
		"Longitude": "72.83534134",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1189,
		"Locality_Name": "Raheja Hospital",
		"Latitude": "19.04664704",
		"Longitude": "72.84270908",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1190,
		"Locality_Name": "Lilavati Hospital And Research Centre",
		"Latitude": "19.05137757",
		"Longitude": "72.82931035",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1191,
		"Locality_Name": "Mahim Fort",
		"Latitude": "19.04212722",
		"Longitude": "72.83818811",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1192,
		"Locality_Name": "Cannossa Special School",
		"Latitude": "19.03785388",
		"Longitude": "72.84400034",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1193,
		"Locality_Name": "Cannossa High School",
		"Latitude": "19.03943591",
		"Longitude": "72.84326821",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1194,
		"Locality_Name": "St. Michael High School",
		"Latitude": "19.0423605",
		"Longitude": "72.84072162",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1195,
		"Locality_Name": "Xavier Institute Of Engineering",
		"Latitude": "19.04540457",
		"Longitude": "72.84164457",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1196,
		"Locality_Name": "St.  Xavier's Technical Institute",
		"Latitude": "19.04493008",
		"Longitude": "72.84104275",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1197,
		"Locality_Name": "Victoria High School",
		"Latitude": "19.03550982",
		"Longitude": "72.84203896",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1198,
		"Locality_Name": "Bombay Scottish School, Mahim",
		"Latitude": "19.03438222",
		"Longitude": "72.83906284",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1199,
		"Locality_Name": "K.J. Khilnani High School & Jr College",
		"Latitude": "19.04253751",
		"Longitude": "72.84332129",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1200,
		"Locality_Name": "Dadar Chowpatty",
		"Latitude": "19.02709869",
		"Longitude": "72.83449551",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1201,
		"Locality_Name": "Mahim Beach",
		"Latitude": "19.04346457",
		"Longitude": "72.83816146",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1202,
		"Locality_Name": "Paradise E. Square Cinema",
		"Latitude": "19.03726647",
		"Longitude": "72.84253443",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1203,
		"Locality_Name": "Shitaladevi Temple",
		"Latitude": "19.03600201",
		"Longitude": "72.84200436",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1205,
		"Locality_Name": "Hazrat Makhdum Ali Mahimi Dargah",
		"Latitude": "19.04010016",
		"Longitude": "72.83880561",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1207,
		"Locality_Name": "St. Michael's Church",
		"Latitude": "19.04290256",
		"Longitude": "72.84059573",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1209,
		"Locality_Name": "Paramount Hotel",
		"Latitude": "19.03879374",
		"Longitude": "72.84177054",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1210,
		"Locality_Name": "Baba Falooda",
		"Latitude": "19.03997396",
		"Longitude": "72.8412577",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1211,
		"Locality_Name": "Mahim Suburban Railway Station (Western)",
		"Latitude": "19.04090693",
		"Longitude": "72.84648811",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1212,
		"Locality_Name": "Mahim - Bus Stop",
		"Latitude": "19.04141816",
		"Longitude": "72.84094668",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1213,
		"Locality_Name": "Mahim - Bus Stop",
		"Latitude": "19.0404296",
		"Longitude": "72.84117811",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1214,
		"Locality_Name": "Mahim(Paradise) - Bus Stop",
		"Latitude": "19.03676282",
		"Longitude": "72.84248662",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1215,
		"Locality_Name": "Shitaladevi Temple - Bus Stop",
		"Latitude": "19.03660389",
		"Longitude": "72.8422448",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1216,
		"Locality_Name": "Shitaladevi Temple - Bus Stop",
		"Latitude": "19.03618998",
		"Longitude": "72.84226244",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1217,
		"Locality_Name": "Shitaladevi Temple Marg - Bus Stop",
		"Latitude": "19.0354937",
		"Longitude": "72.84166203",
		"Station": {
			"id": 16
		}
	},
	{
		"id": 1218,
		"Locality_Name": "Leather Goods Market",
		"Latitude": "19.04906704",
		"Longitude": "72.85518652",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1219,
		"Locality_Name": "Ongc (Oil & Natural Gas Company)",
		"Latitude": "19.05438556",
		"Longitude": "72.84565968",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1220,
		"Locality_Name": "S. L. Raheja Hospital",
		"Latitude": "19.04649604",
		"Longitude": "72.84255902",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1221,
		"Locality_Name": "Sion Hospital",
		"Latitude": "19.03687034",
		"Longitude": "72.86027909",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1222,
		"Locality_Name": "Xavier Institute Of Engineering",
		"Latitude": "19.04527942",
		"Longitude": "72.84166559",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1223,
		"Locality_Name": "St Xavier's Technical Institute",
		"Latitude": "19.04491549",
		"Longitude": "72.8410114",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1224,
		"Locality_Name": "Canossa High School",
		"Latitude": "19.0394298",
		"Longitude": "72.84330317",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1225,
		"Locality_Name": "Maharashtra Nature Park",
		"Latitude": "19.053171",
		"Longitude": "72.86265606",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1226,
		"Locality_Name": "Mahim Beach",
		"Latitude": "19.04361126",
		"Longitude": "72.83805075",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1227,
		"Locality_Name": "Mahim Causeway, Koliwada",
		"Latitude": "19.04739363",
		"Longitude": "72.83801391",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1228,
		"Locality_Name": "Swami Vivekanand Udyan",
		"Latitude": "19.04589872",
		"Longitude": "72.83897111",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1229,
		"Locality_Name": "Jio World Drive",
		"Latitude": "19.05414592",
		"Longitude": "72.85170643",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1230,
		"Locality_Name": "St. Michael's Church",
		"Latitude": "19.04282252",
		"Longitude": "72.84059957",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1231,
		"Locality_Name": "Hazrat Makhdum Shah Baba Radiallahuanhu (Mahim Dargah)",
		"Latitude": "19.04022783",
		"Longitude": "72.83883834",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1232,
		"Locality_Name": "Dharavi Village",
		"Latitude": "19.04733648",
		"Longitude": "72.85413511",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1233,
		"Locality_Name": "Dharavi Sports Complex",
		"Latitude": "19.04827736",
		"Longitude": "72.85950601",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1234,
		"Locality_Name": "District Sports Club",
		"Latitude": "19.04985018",
		"Longitude": "72.85706151",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1235,
		"Locality_Name": "Mahim Fort",
		"Latitude": "19.04229546",
		"Longitude": "72.83808708",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1236,
		"Locality_Name": "Dharavi Bus Stop",
		"Latitude": "19.05045753",
		"Longitude": "72.85745075",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1237,
		"Locality_Name": "Mahim Suburban Railway Station (Western)",
		"Latitude": "19.04329313",
		"Longitude": "72.84652191",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1238,
		"Locality_Name": "Sion Suburban Railway Station (Central)",
		"Latitude": "19.04666237",
		"Longitude": "72.86326259",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1239,
		"Locality_Name": "Dharavi T Junction/Ganpatrao Tapase Chowk - Bus Stop",
		"Latitude": "19.04761954",
		"Longitude": "72.85248481",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1240,
		"Locality_Name": "Dharavi T Junction/Ganpatrao Tapase Chowk - Bus Stop",
		"Latitude": "19.04756163",
		"Longitude": "72.85283366",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1241,
		"Locality_Name": "Banwari Compound - Bus Stop",
		"Latitude": "19.04565107",
		"Longitude": "72.84690037",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1242,
		"Locality_Name": "Banwari Compound - Bus Stop",
		"Latitude": "19.04547731",
		"Longitude": "72.84729826",
		"Station": {
			"id": 17
		}
	},
	{
		"id": 1243,
		"Locality_Name": "Jio Mall",
		"Latitude": "19.05390817",
		"Longitude": "72.85174032",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1244,
		"Locality_Name": "Income Tax Office",
		"Latitude": "19.06254687",
		"Longitude": "72.86860726",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1245,
		"Locality_Name": "Reserve Bank Of India",
		"Latitude": "19.057668",
		"Longitude": "72.85377857",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1246,
		"Locality_Name": "Family Court",
		"Latitude": "19.05561097",
		"Longitude": "72.8513484",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1247,
		"Locality_Name": "MMRDA Old Building",
		"Latitude": "19.05511551",
		"Longitude": "72.8518592",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1248,
		"Locality_Name": "Mumbai Metropolitan Region Development Authority",
		"Latitude": "19.05379276",
		"Longitude": "72.85208436",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1249,
		"Locality_Name": "Mumbai Metro Rail Corporation Limited",
		"Latitude": "19.05638831",
		"Longitude": "72.85472583",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1250,
		"Locality_Name": "Maharashtra Housing And Area Development Authority",
		"Latitude": "19.05507175",
		"Longitude": "72.84728341",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1251,
		"Locality_Name": "Labour Court",
		"Latitude": "19.06131341",
		"Longitude": "72.8500281",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1252,
		"Locality_Name": "National Stock Exchange",
		"Latitude": "19.05991407",
		"Longitude": "72.86023229",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1253,
		"Locality_Name": "NABARD Head Office",
		"Latitude": "19.06441906",
		"Longitude": "72.86249305",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1254,
		"Locality_Name": "BKC Police Station",
		"Latitude": "19.06457539",
		"Longitude": "72.86028957",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1255,
		"Locality_Name": "Collector MSD",
		"Latitude": "19.06146053",
		"Longitude": "72.8500455",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1256,
		"Locality_Name": "Securities and Exchange Board of India (SEBI)",
		"Latitude": "19.05920544",
		"Longitude": "72.86134875",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1257,
		"Locality_Name": "Guru Nanak Hospital",
		"Latitude": "19.05963428",
		"Longitude": "72.85274555",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1259,
		"Locality_Name": "Chetana'S Institute Of Management And Research",
		"Latitude": "19.06099363",
		"Longitude": "72.84807364",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1260,
		"Locality_Name": "Chetana'S H.S College Of Commerce & Economics.",
		"Latitude": "19.06126778",
		"Longitude": "72.84851184",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1261,
		"Locality_Name": "Asian Heart Institute",
		"Latitude": "19.06529106",
		"Longitude": "72.86083192",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1262,
		"Locality_Name": "RNA Corporate Park",
		"Latitude": "19.0610309",
		"Longitude": "72.85092785",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1263,
		"Locality_Name": "Wockhardt Tower",
		"Latitude": "19.06107325",
		"Longitude": "72.85978208",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1264,
		"Locality_Name": "Reliance Jio Infocomm Limited",
		"Latitude": "19.06162632",
		"Longitude": "72.86009164",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1265,
		"Locality_Name": "IL&FS",
		"Latitude": "19.06305932",
		"Longitude": "72.86050458",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1266,
		"Locality_Name": "ICICI Bank",
		"Latitude": "19.06412607",
		"Longitude": "72.86165769",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1267,
		"Locality_Name": "TCG Financial Centre",
		"Latitude": "19.05296159",
		"Longitude": "72.85085777",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1268,
		"Locality_Name": "Income Tax Office (Towards MTNL)",
		"Latitude": "19.05916447",
		"Longitude": "72.85444966",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1269,
		"Locality_Name": "Income Tax Office(Towards Kala Nagar)",
		"Latitude": "19.05894059",
		"Longitude": "72.85470397",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1270,
		"Locality_Name": "Tata Colony (Towards MTNL)",
		"Latitude": "19.06000368",
		"Longitude": "72.85647889",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1271,
		"Locality_Name": "Tata Colony (Towards Kala Nagar)",
		"Latitude": "19.06026091",
		"Longitude": "72.85795512",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1272,
		"Locality_Name": "Reserve Bank of India(Towards Kala Nagar)",
		"Latitude": "19.05760519",
		"Longitude": "72.85326289",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1273,
		"Locality_Name": "Reserve Bank of India (Towards MTNL)",
		"Latitude": "19.05789104",
		"Longitude": "72.85308203",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1274,
		"Locality_Name": "BKC Dimond Market",
		"Latitude": "19.06447824",
		"Longitude": "72.86372702",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1275,
		"Locality_Name": "Hallamrk Business Plazza",
		"Latitude": "19.06048873",
		"Longitude": "72.85191833",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1276,
		"Locality_Name": "Office Of District Collector, Mumbai Suburban",
		"Latitude": "19.06154489",
		"Longitude": "72.84998357",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1277,
		"Locality_Name": "Directorate Of Maharashtra Fire Service",
		"Latitude": "19.07530528",
		"Longitude": "72.85717719",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1278,
		"Locality_Name": "NIRON Hospital",
		"Latitude": "19.07724075",
		"Longitude": "72.8581255",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1279,
		"Locality_Name": "Shankarrao Chavan Bhavan",
		"Latitude": "19.06939384",
		"Longitude": "72.85954591",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1280,
		"Locality_Name": "Chetana'S Institute Of Management And Research",
		"Latitude": "19.06096208",
		"Longitude": "72.84805238",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1281,
		"Locality_Name": "Raje Sambhaji Vidylay",
		"Latitude": "19.07499796",
		"Longitude": "72.84553397",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1282,
		"Locality_Name": "Mumbai University Gate No. 2",
		"Latitude": "19.07374375",
		"Longitude": "72.85303238",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1283,
		"Locality_Name": "Bombay College Of Pharmacy India",
		"Latitude": "19.07707967",
		"Longitude": "72.86016261",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1284,
		"Locality_Name": "Ascend International School",
		"Latitude": "19.0681125",
		"Longitude": "72.85091961",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1285,
		"Locality_Name": "Indian Education Society New English School",
		"Latitude": "19.06708957",
		"Longitude": "72.84979079",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1286,
		"Locality_Name": "Dr. Baliram Hiray College Of Architecture",
		"Latitude": "19.06649485",
		"Longitude": "72.84930609",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1287,
		"Locality_Name": "Cardinal Gracias High School",
		"Latitude": "19.06682524",
		"Longitude": "72.84749538",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1288,
		"Locality_Name": "MPSP Singh College",
		"Latitude": "19.07004984",
		"Longitude": "72.84745705",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1289,
		"Locality_Name": "Centre for the Study of Social Change (CSSC)",
		"Latitude": "19.06965853",
		"Longitude": "72.84982343",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1290,
		"Locality_Name": "Uttar Bharatiya Sangh College Of Commerce & Science",
		"Latitude": "19.0706975",
		"Longitude": "72.84925812",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1291,
		"Locality_Name": "University Of Mumbai",
		"Latitude": "19.07304997",
		"Longitude": "72.86079853",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1292,
		"Locality_Name": "Dr. Babasaheb Ambedkar Udyan",
		"Latitude": "19.06055501",
		"Longitude": "72.84925657",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1293,
		"Locality_Name": "Sanghamitra Buddha Vihar",
		"Latitude": "19.06976819",
		"Longitude": "72.84778461",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1294,
		"Locality_Name": "Shree Harigurugram",
		"Latitude": "19.06714246",
		"Longitude": "72.84945247",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1295,
		"Locality_Name": "Church Of St. Joseph The Worker",
		"Latitude": "19.06729533",
		"Longitude": "72.84756815",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1296,
		"Locality_Name": "Sethia Grandeur",
		"Latitude": "19.070675",
		"Longitude": "72.84841605",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1297,
		"Locality_Name": "Kanakia Paris",
		"Latitude": "19.06696691",
		"Longitude": "72.85168597",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1298,
		"Locality_Name": "Bandra Govt. Colony",
		"Latitude": "19.060586",
		"Longitude": "72.85044589",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1299,
		"Locality_Name": "AITA Trust Tennis Courts",
		"Latitude": "19.073399",
		"Longitude": "72.85129621",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1301,
		"Locality_Name": "Bandra Railway Staation",
		"Latitude": "19.05480999",
		"Longitude": "72.84060776",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1302,
		"Locality_Name": "Khar Road Suburban Railway Station (Western)",
		"Latitude": "19.06731516",
		"Longitude": "72.84172757",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1303,
		"Locality_Name": "Porsche Centre Mumbai",
		"Latitude": "19.08544496",
		"Longitude": "72.83487655",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1304,
		"Locality_Name": "Vakola Police Station",
		"Latitude": "19.0807703",
		"Longitude": "72.84734541",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1305,
		"Locality_Name": "V. N. Desai Hospital",
		"Latitude": "19.07899309",
		"Longitude": "72.84477663",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1306,
		"Locality_Name": "R. K. Hospital",
		"Latitude": "19.08074401",
		"Longitude": "72.84207344",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1308,
		"Locality_Name": "Grand Hyatt Mumbai",
		"Latitude": "19.07698099",
		"Longitude": "72.85112369",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1309,
		"Locality_Name": "St. Anthony'S Boys High School",
		"Latitude": "19.07990374",
		"Longitude": "72.85320184",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1310,
		"Locality_Name": "BMC Vakola School",
		"Latitude": "19.08000119",
		"Longitude": "72.85065723",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1311,
		"Locality_Name": "Patuck College",
		"Latitude": "19.08117829",
		"Longitude": "72.84964843",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1312,
		"Locality_Name": "DDB Mudra Group",
		"Latitude": "19.07622539",
		"Longitude": "72.8514785",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1313,
		"Locality_Name": "JMC Projects India Limited (Kalpataru)",
		"Latitude": "19.07645144",
		"Longitude": "72.85099297",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1314,
		"Locality_Name": "Asian Paints",
		"Latitude": "19.0766139",
		"Longitude": "72.85043496",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1315,
		"Locality_Name": "Kalpataru Inspire",
		"Latitude": "19.07540893",
		"Longitude": "72.8507017",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1316,
		"Locality_Name": "Reliance Centre",
		"Latitude": "19.08369033",
		"Longitude": "72.84545671",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1317,
		"Locality_Name": "Dinker Patel Garden",
		"Latitude": "19.07917379",
		"Longitude": "72.84397372",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1318,
		"Locality_Name": "St. Anthony Church / Vakola Church",
		"Latitude": "19.07997064",
		"Longitude": "72.85280475",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1319,
		"Locality_Name": "Western Express Highway",
		"Latitude": "19.08948246",
		"Longitude": "72.8436706",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1320,
		"Locality_Name": "Santacurz Suburban Railway Station (Western)",
		"Latitude": "19.08218345",
		"Longitude": "72.84176421",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1321,
		"Locality_Name": "Vakola Police Station (Towards Andheri)  ",
		"Latitude": "19.08237894",
		"Longitude": "72.84626948",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1322,
		"Locality_Name": "Vakola Police Station - Hanuman Mandir (Towards Kala Nagar)",
		"Latitude": "19.07917028",
		"Longitude": "72.84706756",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1323,
		"Locality_Name": "Vakola Police Station(Hanuman Mandir) (Towards Andheri)",
		"Latitude": "19.07875717",
		"Longitude": "72.84669956",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1324,
		"Locality_Name": "Vakola Police Station (Towards Kalina)",
		"Latitude": "19.08036741",
		"Longitude": "72.84957857",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1325,
		"Locality_Name": "Vakola Police Station (Towards Santacruz Station)",
		"Latitude": "19.0800735",
		"Longitude": "72.84956261",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1326,
		"Locality_Name": "Vakola Police Station - Roop Cinema(Towards Kalina)",
		"Latitude": "19.08037299",
		"Longitude": "72.84549824",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1327,
		"Locality_Name": "Vakola Police Station - Roop Cinema (Towards Kalina)",
		"Latitude": "19.08054533",
		"Longitude": "72.84608342",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1328,
		"Locality_Name": "Maratha Colony (Towards Vidyanagari)",
		"Latitude": "19.0752029",
		"Longitude": "72.84703758",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1329,
		"Locality_Name": "Maratha Colony (Towards Vakola)",
		"Latitude": "19.07511958",
		"Longitude": "72.84662089",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1330,
		"Locality_Name": "ATC Tower",
		"Latitude": "19.09435388",
		"Longitude": "72.8552087",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1331,
		"Locality_Name": "Santacruz Airport Post Office",
		"Latitude": "19.0952933",
		"Longitude": "72.85534856",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1332,
		"Locality_Name": "Taj Santacruz Hotel",
		"Latitude": "19.09304332",
		"Longitude": "72.85431157",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1333,
		"Locality_Name": "Hotel Sahar Star",
		"Latitude": "19.09625669",
		"Longitude": "72.8538759",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1334,
		"Locality_Name": "Hotel Airport International",
		"Latitude": "19.09640048",
		"Longitude": "72.85417276",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1335,
		"Locality_Name": "Hotel Bawa International",
		"Latitude": "19.09648666",
		"Longitude": "72.85357971",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1336,
		"Locality_Name": "Ibis Hotel",
		"Latitude": "19.09664986",
		"Longitude": "72.85349371",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1337,
		"Locality_Name": "Hotel Atithi",
		"Latitude": "19.09688743",
		"Longitude": "72.85410668",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1338,
		"Locality_Name": "The Orchid Ecotel Hotel",
		"Latitude": "19.09709941",
		"Longitude": "72.85496642",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1339,
		"Locality_Name": "Hotel Airlink",
		"Latitude": "19.0979269",
		"Longitude": "72.85445108",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1340,
		"Locality_Name": "Nandgiri State Guest House",
		"Latitude": "19.09827744",
		"Longitude": "72.85390576",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1341,
		"Locality_Name": "Avion Hotel",
		"Latitude": "19.09618392",
		"Longitude": "72.85254741",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1342,
		"Locality_Name": "Hotel Aircraft International",
		"Latitude": "19.09581008",
		"Longitude": "72.85189117",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1343,
		"Locality_Name": "Dixit Road Junior College Of Science",
		"Latitude": "19.09840817",
		"Longitude": "72.84984758",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1344,
		"Locality_Name": "Sathaye College",
		"Latitude": "19.09891632",
		"Longitude": "72.85057279",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1345,
		"Locality_Name": "M.L. Dahanukar College Of Commerce",
		"Latitude": "19.09902252",
		"Longitude": "72.85149204",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1347,
		"Locality_Name": "Electric Vehicle Charging Station",
		"Latitude": "19.09489239",
		"Longitude": "72.85614818",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1348,
		"Locality_Name": "CSMIA T1 (Domestic) Airport",
		"Latitude": "19.09333628",
		"Longitude": "72.85573784",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1349,
		"Locality_Name": "Vile Parle Suburban Railway Station (Western)",
		"Latitude": "19.09868076",
		"Longitude": "72.84430944",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1350,
		"Locality_Name": "Domestic Airport Terminal 1-A",
		"Latitude": "19.09345428",
		"Longitude": "72.85590415",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1351,
		"Locality_Name": "Domestic Airport Terminal 1-B",
		"Latitude": "19.09345343",
		"Longitude": "72.8527629",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1352,
		"Locality_Name": "Domestic Airport Junction (Towards Andheri / Vile Parle Station)",
		"Latitude": "19.09433295",
		"Longitude": "72.85171512",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1353,
		"Locality_Name": "Gujarat Society/Dayaldas Road (Towards Vile Parle Station)",
		"Latitude": "19.09699411",
		"Longitude": "72.85083646",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1354,
		"Locality_Name": "Gujarat Society / Dayaldas Road (Towards Vakola)",
		"Latitude": "19.09702871",
		"Longitude": "72.85114222",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1355,
		"Locality_Name": "Air India Hanger Narrow Body",
		"Latitude": "19.10052475",
		"Longitude": "72.86041019",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1356,
		"Locality_Name": "Air India Wide Body Aircraft Service Hangar",
		"Latitude": "19.10084552",
		"Longitude": "72.85987259",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1357,
		"Locality_Name": "Sahar Cargo Estate",
		"Latitude": "19.10658072",
		"Longitude": "72.86370343",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1358,
		"Locality_Name": "Sahar Cargo Warehouse",
		"Latitude": "19.10656512",
		"Longitude": "72.86385253",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1359,
		"Locality_Name": "Oberol Flight Services",
		"Latitude": "19.1054466",
		"Longitude": "72.87297308",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1360,
		"Locality_Name": "Air India Air Transport Services Ltd",
		"Latitude": "19.0982886",
		"Longitude": "72.87123529",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1361,
		"Locality_Name": "Chefair Catering Service",
		"Latitude": "19.10214013",
		"Longitude": "72.87077296",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1362,
		"Locality_Name": "Blue Dart",
		"Latitude": "19.10524388",
		"Longitude": "72.87005498",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1363,
		"Locality_Name": "Jet Airways",
		"Latitude": "19.10488785",
		"Longitude": "72.87059873",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1364,
		"Locality_Name": "Proposed Airport City Complex",
		"Latitude": "19.09725347",
		"Longitude": "72.87534414",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1365,
		"Locality_Name": "Cargo Complex",
		"Latitude": "19.09795313",
		"Longitude": "72.86946526",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1366,
		"Locality_Name": "Indian Meteorological Department, Rsrw",
		"Latitude": "19.10117743",
		"Longitude": "72.85839565",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1367,
		"Locality_Name": "Hotel Le Grande",
		"Latitude": "19.10559885",
		"Longitude": "72.86261549",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1368,
		"Locality_Name": "ITC Maratha",
		"Latitude": "19.10326873",
		"Longitude": "72.87005323",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1369,
		"Locality_Name": "Hilton Mumbai International Airport",
		"Latitude": "19.10437833",
		"Longitude": "72.87058046",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1370,
		"Locality_Name": "Hyatt Regency Mumbai",
		"Latitude": "19.10327271",
		"Longitude": "72.8715155",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1371,
		"Locality_Name": "Bombay Cambridge International School",
		"Latitude": "19.10553481",
		"Longitude": "72.8624182",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1372,
		"Locality_Name": "Prime Corporate Park",
		"Latitude": "19.10559304",
		"Longitude": "72.86947114",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1373,
		"Locality_Name": "Sahar P&T Colony",
		"Latitude": "19.10088903",
		"Longitude": "72.8621654",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1374,
		"Locality_Name": "Sahar Village",
		"Latitude": "19.10082871",
		"Longitude": "72.86754925",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1375,
		"Locality_Name": "Chakala Metro Station (Line-1)",
		"Latitude": "19.11177235",
		"Longitude": "72.86800172",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1376,
		"Locality_Name": "EV Dock Charging Station",
		"Latitude": "19.10347301",
		"Longitude": "72.86260506",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1377,
		"Locality_Name": "Ware House (Towards Andheri / WEH)",
		"Latitude": "19.10274138",
		"Longitude": "72.8668762",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1378,
		"Locality_Name": "Ware House (Towards CSMIA - T2)",
		"Latitude": "19.10300797",
		"Longitude": "72.86689367",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1379,
		"Locality_Name": "Ware House (Towards JB Nagar)",
		"Latitude": "19.1031239",
		"Longitude": "72.86644085",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1380,
		"Locality_Name": "Post and Tar Colony (Towards Sahar Cargo Complex)",
		"Latitude": "19.10151962",
		"Longitude": "72.86345379",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1381,
		"Locality_Name": "Post and Tar Colony (Towards Andheri / WEH)",
		"Latitude": "19.10141972",
		"Longitude": "72.86320565",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1382,
		"Locality_Name": "Air India Air Transport Services Ltd",
		"Latitude": "19.09837306",
		"Longitude": "72.87104845",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1383,
		"Locality_Name": "Ambassador's Sky Chef",
		"Latitude": "19.10325139",
		"Longitude": "72.87494728",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1384,
		"Locality_Name": "Bureau Of Civil Aviation Security",
		"Latitude": "19.10814394",
		"Longitude": "72.8565553",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1385,
		"Locality_Name": "Sahar Police Station",
		"Latitude": "19.10001695",
		"Longitude": "72.87029356",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1386,
		"Locality_Name": "Airport Health Organization",
		"Latitude": "19.10317415",
		"Longitude": "72.87665072",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1387,
		"Locality_Name": "JW Marriott Hotel",
		"Latitude": "19.10315776",
		"Longitude": "72.87719762",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1388,
		"Locality_Name": "Waterstones Hotel",
		"Latitude": "19.1049453",
		"Longitude": "72.87662116",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1389,
		"Locality_Name": "The Lalit Hotel",
		"Latitude": "19.10597301",
		"Longitude": "72.87528934",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1390,
		"Locality_Name": "Hyatt Regency Mumbai",
		"Latitude": "19.10338315",
		"Longitude": "72.87152634",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1391,
		"Locality_Name": "ITC Maratha",
		"Latitude": "19.10321277",
		"Longitude": "72.8700607",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1392,
		"Locality_Name": "Hilton Mumbai International Airport",
		"Latitude": "19.10435403",
		"Longitude": "72.87053597",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1393,
		"Locality_Name": "The Leela Hotel",
		"Latitude": "19.10874525",
		"Longitude": "72.87366948",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1394,
		"Locality_Name": "Chefair Catering Service",
		"Latitude": "19.10219273",
		"Longitude": "72.87108711",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1395,
		"Locality_Name": "Jet Airways",
		"Latitude": "19.10487485",
		"Longitude": "72.87064325",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1396,
		"Locality_Name": "Blue Dart Centre",
		"Latitude": "19.10529476",
		"Longitude": "72.87002084",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1397,
		"Locality_Name": "Prime Corporate Park",
		"Latitude": "19.10558781",
		"Longitude": "72.86945998",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1398,
		"Locality_Name": "CSMIA Terminal 2",
		"Latitude": "19.10032915",
		"Longitude": "72.8763553",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1399,
		"Locality_Name": "Airport Road Metro Station (Line-1)",
		"Latitude": "19.10972158",
		"Longitude": "72.874825",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1400,
		"Locality_Name": "CSIA",
		"Latitude": "19.10155378",
		"Longitude": "72.87258921",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1401,
		"Locality_Name": "Sahar Police Station",
		"Latitude": "19.10198924",
		"Longitude": "72.87628239",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1402,
		"Locality_Name": "Indian Oil (Towards Sahar Cargo Complex/WEH)",
		"Latitude": "19.10300879",
		"Longitude": "72.8716358",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1404,
		"Locality_Name": "Tata Power Charging Station",
		"Latitude": "19.1028031",
		"Longitude": "72.87358667",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1405,
		"Locality_Name": "MCGM Market",
		"Latitude": "19.11362605",
		"Longitude": "72.87667415",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1406,
		"Locality_Name": "MIDC Industrial Area",
		"Latitude": "19.11989867",
		"Longitude": "72.87290961",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1407,
		"Locality_Name": "Udyog Sarthi Marol Industrial Area Mahakali Caves Road Andheri East",
		"Latitude": "19.11750268",
		"Longitude": "72.86301389",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1408,
		"Locality_Name": "Marol Fire Brigade",
		"Latitude": "19.10944591",
		"Longitude": "72.87773719",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1409,
		"Locality_Name": "Marol Naka Station (Line-1 )",
		"Latitude": "19.1082258",
		"Longitude": "72.87896795",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1410,
		"Locality_Name": "Seven Hills Hospital",
		"Latitude": "19.11768572",
		"Longitude": "72.87883205",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1411,
		"Locality_Name": "Hotel Sahar Garden",
		"Latitude": "19.10896165",
		"Longitude": "72.87853929",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1412,
		"Locality_Name": "Hotel Leafio Marigold",
		"Latitude": "19.11052649",
		"Longitude": "72.8793206",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1413,
		"Locality_Name": "Hotel Silver Inn",
		"Latitude": "19.11097578",
		"Longitude": "72.87875029",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1414,
		"Locality_Name": "Hotel Ashwin",
		"Latitude": "19.11009681",
		"Longitude": "72.8784179",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1415,
		"Locality_Name": "Mirage Hotel",
		"Latitude": "19.10887184",
		"Longitude": "72.87709965",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1416,
		"Locality_Name": "The Leela",
		"Latitude": "19.10880577",
		"Longitude": "72.87376095",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1417,
		"Locality_Name": "The Lalit Residency",
		"Latitude": "19.10599769",
		"Longitude": "72.87529991",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1418,
		"Locality_Name": "Waterstones Hotel",
		"Latitude": "19.1052333",
		"Longitude": "72.87713088",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1419,
		"Locality_Name": "Hotel Radisson Blue",
		"Latitude": "19.11020836",
		"Longitude": "72.87848069",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1420,
		"Locality_Name": "Pearl Academy",
		"Latitude": "19.10826733",
		"Longitude": "72.88056663",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1421,
		"Locality_Name": "Marol BMC School",
		"Latitude": "19.11033842",
		"Longitude": "72.87708641",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1422,
		"Locality_Name": "St. John The Evangelist High School",
		"Latitude": "19.11189171",
		"Longitude": "72.87529024",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1423,
		"Locality_Name": "Smartworks - Fleet House",
		"Latitude": "19.10846679",
		"Longitude": "72.87899576",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1424,
		"Locality_Name": "St. John The Evangelist Church",
		"Latitude": "19.1127669",
		"Longitude": "72.87620452",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1425,
		"Locality_Name": "Marol Naka/Mata Ramabai Ambedkar Chowk (Towards Marol Maroshi)",
		"Latitude": "19.11059115",
		"Longitude": "72.87849573",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1426,
		"Locality_Name": "Marol Naka/Mata Ramabai Ambedkar Chowk (Towards CSMIA/JB Nagar)",
		"Latitude": "19.10872488",
		"Longitude": "72.87746808",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1427,
		"Locality_Name": "Marol Naka/Mata Ramabai Ambedkar Chowk (Towards Saki Naka)",
		"Latitude": "19.10800739",
		"Longitude": "72.88044214",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1428,
		"Locality_Name": "Mittal Estate - Bus Stop",
		"Latitude": "19.10751889",
		"Longitude": "72.88068314",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1429,
		"Locality_Name": "EV DOCK Charging Station",
		"Latitude": "19.10807956",
		"Longitude": "72.88197347",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1430,
		"Locality_Name": "MCGM Market",
		"Latitude": "19.11360739",
		"Longitude": "72.87667487",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1431,
		"Locality_Name": "Passport Seva Kendra",
		"Latitude": "19.11938126",
		"Longitude": "72.87571412",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1432,
		"Locality_Name": "Mtnl Office",
		"Latitude": "19.11813171",
		"Longitude": "72.86899239",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1433,
		"Locality_Name": "Bureau Of Indian Standards",
		"Latitude": "19.11956639",
		"Longitude": "72.86950363",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1434,
		"Locality_Name": "Sme Chamber Of India (Small & Medium Business Development Chamber Of India",
		"Latitude": "19.12052481",
		"Longitude": "72.87043513",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1435,
		"Locality_Name": "Head Office Midc",
		"Latitude": "19.11753743",
		"Longitude": "72.86302535",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1436,
		"Locality_Name": "Seven Hills Hospital",
		"Latitude": "19.11768084",
		"Longitude": "72.87883283",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1437,
		"Locality_Name": "Hotel Cosmo",
		"Latitude": "19.11994334",
		"Longitude": "72.87803672",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1438,
		"Locality_Name": "Hotel Suncity Residency",
		"Latitude": "19.11919719",
		"Longitude": "72.87401966",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1439,
		"Locality_Name": "P.D. Hinduja College Of Nursing.",
		"Latitude": "19.11445729",
		"Longitude": "72.87115187",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1440,
		"Locality_Name": "Ryan Global School",
		"Latitude": "19.11830292",
		"Longitude": "72.8727316",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1441,
		"Locality_Name": "ESI Post Graduate Institute of Medical Science and Research",
		"Latitude": "19.1185715",
		"Longitude": "72.86697869",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1442,
		"Locality_Name": "Hasnath School",
		"Latitude": "19.11554268",
		"Longitude": "72.87703558",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1443,
		"Locality_Name": "ESIC Branch Office",
		"Latitude": "19.11765099",
		"Longitude": "72.87276137",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1444,
		"Locality_Name": "Ackruti Trade Centre",
		"Latitude": "19.11749964",
		"Longitude": "72.87126119",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1445,
		"Locality_Name": "Ackruti Star",
		"Latitude": "19.11876461",
		"Longitude": "72.87057991",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1446,
		"Locality_Name": "Ackruti Centre Point",
		"Latitude": "19.11880519",
		"Longitude": "72.87004179",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1447,
		"Locality_Name": "Midc Industrial Area",
		"Latitude": "19.11974002",
		"Longitude": "72.87320801",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1448,
		"Locality_Name": "Andheri Railway Station",
		"Latitude": "19.12006535",
		"Longitude": "72.84640993",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1449,
		"Locality_Name": "Andheri Bus Depot",
		"Latitude": "19.12006535",
		"Longitude": "72.84640993",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1450,
		"Locality_Name": "Mumbai Metro Line 1 Station",
		"Latitude": "19.12006535",
		"Longitude": "72.84640993",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1451,
		"Locality_Name": "Electronic Regional Test Laboratory",
		"Latitude": "19.12619764",
		"Longitude": "72.87360483",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1452,
		"Locality_Name": "SEEPZ Economic Zone",
		"Latitude": "19.12498187",
		"Longitude": "72.87323816",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1455,
		"Locality_Name": "Directi Seepz Office",
		"Latitude": "19.12792292",
		"Longitude": "72.87853068",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1456,
		"Locality_Name": "National Test House (Western Railway)",
		"Latitude": "19.12380872",
		"Longitude": "72.87187992",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1457,
		"Locality_Name": "Head office MIDC",
		"Latitude": "19.12366685",
		"Longitude": "72.87535519",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1458,
		"Locality_Name": "Udyog Sarthi Marol Industrial Area Mahakali Caves Road Andheri East",
		"Latitude": "19.11752897",
		"Longitude": "72.86302549",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1459,
		"Locality_Name": "Dr. Susan Sodder Pvt. Hospital",
		"Latitude": "19.12513133",
		"Longitude": "72.86562421",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1460,
		"Locality_Name": "Holy Spirit Hospital",
		"Latitude": "19.12734961",
		"Longitude": "72.86729121",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1461,
		"Locality_Name": "Sun City Hotel",
		"Latitude": "19.12858074",
		"Longitude": "72.87783066",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1462,
		"Locality_Name": "St. Arnold'S High School & Junior College",
		"Latitude": "19.12444114",
		"Longitude": "72.86697061",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1463,
		"Locality_Name": "Canossa High School",
		"Latitude": "19.12529726",
		"Longitude": "72.86597353",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1464,
		"Locality_Name": "Institute Of Indian Culture",
		"Latitude": "19.12515598",
		"Longitude": "72.86592154",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1465,
		"Locality_Name": "TCS Mumbai SEEPZ SDF III",
		"Latitude": "19.12689469",
		"Longitude": "72.87525446",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1466,
		"Locality_Name": "Unidesign Jewellery India Pvt. Ltd.",
		"Latitude": "19.11584958",
		"Longitude": "72.85819326",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1467,
		"Locality_Name": "Adani Electricity Management Institute",
		"Latitude": "19.12976406",
		"Longitude": "72.88201067",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1468,
		"Locality_Name": "Sacred Heart Church",
		"Latitude": "19.12463961",
		"Longitude": "72.86647027",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1469,
		"Locality_Name": "Gyan Ashram",
		"Latitude": "19.12301651",
		"Longitude": "72.86465804",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1470,
		"Locality_Name": "SEEPZ Bus Depot",
		"Latitude": "19.12627435",
		"Longitude": "72.87363606",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1471,
		"Locality_Name": "SEEPZ - Bus Stop",
		"Latitude": "19.12430338",
		"Longitude": "72.87229106",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1472,
		"Locality_Name": "SEEPZ - Bus Stop",
		"Latitude": "19.12421125",
		"Longitude": "72.87240733",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1473,
		"Locality_Name": "SEEPZ - Bus Stop",
		"Latitude": "19.1279174",
		"Longitude": "72.87487402",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1474,
		"Locality_Name": "C Cross Road Junction - Bus Stop",
		"Latitude": "19.12354306",
		"Longitude": "72.87199271",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1475,
		"Locality_Name": "C Cross Road Junction - Bus Stop",
		"Latitude": "19.1232024",
		"Longitude": "72.87135533",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1477,
		"Locality_Name": "C Cross Road Junction - Bus Stop",
		"Latitude": "19.12292332",
		"Longitude": "72.87203879",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1478,
		"Locality_Name": "Marol Police Camp",
		"Latitude": "19.1240849",
		"Longitude": "72.8830333",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1479,
		"Locality_Name": "Directi SEEPZ Office",
		"Latitude": "19.12767446",
		"Longitude": "72.87863336",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1481,
		"Locality_Name": "Dr. Susan Sodder Pvt. Hospital",
		"Latitude": "19.12491168",
		"Longitude": "72.86556504",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1482,
		"Locality_Name": "Sun City Hotel",
		"Latitude": "19.1285024",
		"Longitude": "72.87784163",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1483,
		"Locality_Name": "Indian Educational Society",
		"Latitude": "19.12802878",
		"Longitude": "72.88664371",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1484,
		"Locality_Name": "Oberoi International School, Jvlr Campus",
		"Latitude": "19.14009593",
		"Longitude": "72.86732779",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1485,
		"Locality_Name": "Aarey Picnic Point",
		"Latitude": "19.1366713",
		"Longitude": "72.88238606",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1486,
		"Locality_Name": "Adani Electricity Management Institute",
		"Latitude": "19.12986485",
		"Longitude": "72.88194499",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1487,
		"Locality_Name": "L&T Headquarters",
		"Latitude": "19.12687828",
		"Longitude": "72.89054469",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1488,
		"Locality_Name": "SEEPZ Office",
		"Latitude": "19.12372754",
		"Longitude": "72.87528628",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1489,
		"Locality_Name": "Aarey Om Temple",
		"Latitude": "19.13162561",
		"Longitude": "72.88768435",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1490,
		"Locality_Name": "Shree Shubhanand Aashram Powai",
		"Latitude": "19.1287018",
		"Longitude": "72.88663365",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1492,
		"Locality_Name": "Jogeshwari Vikhroli Link Road",
		"Latitude": "19.12947982",
		"Longitude": "72.88351722",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1493,
		"Locality_Name": "Seepz Village Metro Station (Line 6)",
		"Latitude": "19.12937951",
		"Longitude": "72.88239702",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1494,
		"Locality_Name": "Jogeshwari Metro Station (East) Line 7",
		"Latitude": "19.14271361",
		"Longitude": "72.85528647",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1495,
		"Locality_Name": "Adani Electicity Management Institute",
		"Latitude": "19.12954857",
		"Longitude": "72.88242747",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1496,
		"Locality_Name": "Reliance Energy Training Centre",
		"Latitude": "19.12927274",
		"Longitude": "72.88153077",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1497,
		"Locality_Name": "Cardinal Gracias School Teachers Colony (Towards Kala Nagar)",
		"Latitude": "19.06830365",
		"Longitude": "72.8469418",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1498,
		"Locality_Name": "Cardinal Gracias School Teachers Colony (Towards Vakola)",
		"Latitude": "19.06821761",
		"Longitude": "72.84653972",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1499,
		"Locality_Name": "Kherwadi Police Station (Towards Tata Colony)",
		"Latitude": "19.06591594",
		"Longitude": "72.84939918",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1500,
		"Locality_Name": "Kherwadi Police Station (Towards Kala Nagar)",
		"Latitude": "19.06477418",
		"Longitude": "72.85021415",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1501,
		"Locality_Name": "Gautam Nagar (Towards Chakala)",
		"Latitude": "19.11854671",
		"Longitude": "72.87012072",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1502,
		"Locality_Name": "Gautam Nagar (Towards SEEPZ)",
		"Latitude": "19.11853237",
		"Longitude": "72.86976795",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1503,
		"Locality_Name": "Indian Oil (Towards CSMIA)",
		"Latitude": "19.10331613",
		"Longitude": "72.87123845",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1504,
		"Locality_Name": "Ambassador Hotel (Towards Marol Naka)",
		"Latitude": "19.10403915",
		"Longitude": "72.87439828",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1506,
		"Locality_Name": "Domestic Airport Junction (Towards Vakola)",
		"Latitude": "19.09363999",
		"Longitude": "72.85175496",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1507,
		"Locality_Name": "Vile Parle Police Station (Towards Vile Parle Station)",
		"Latitude": "19.09617097",
		"Longitude": "72.85428089",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1508,
		"Locality_Name": "Domestic Airport Taxi Pickup Point",
		"Latitude": "19.09289968",
		"Longitude": "72.85562833",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1509,
		"Locality_Name": "Domestic Airport Parking",
		"Latitude": "19.09402505",
		"Longitude": "72.85600906",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1510,
		"Locality_Name": "Santacruz Station (East) Bus Station",
		"Latitude": "19.08164801",
		"Longitude": "72.84258894",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1511,
		"Locality_Name": "Bandra Colony Bus Station",
		"Latitude": "19.06159518",
		"Longitude": "72.85082144",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1514,
		"Locality_Name": "Hallmark Business Plaza",
		"Latitude": "19.0606135",
		"Longitude": "72.85227311",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1515,
		"Locality_Name": "Bank Of India Head Office",
		"Latitude": "19.0610129",
		"Longitude": "72.86170074",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1516,
		"Locality_Name": "Central GST Bhavan",
		"Latitude": "19.05796968",
		"Longitude": "72.85557645",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1517,
		"Locality_Name": "Food and Drugs Administration",
		"Latitude": "19.05838751",
		"Longitude": "72.85294383",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1519,
		"Locality_Name": "Asian Heart Institute",
		"Latitude": "19.06529106",
		"Longitude": "72.86083192",
		"Station": {
			"id": 18
		}
	},
	{
		"id": 1520,
		"Locality_Name": "Kalpataru Inspire",
		"Latitude": "19.07525589",
		"Longitude": "72.85077635",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1521,
		"Locality_Name": "Kalpataru Synergy",
		"Latitude": "19.07624352",
		"Longitude": "72.85062526",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1522,
		"Locality_Name": "Hotel Grand Hyatt Mumbai",
		"Latitude": "19.07714878",
		"Longitude": "72.85158455",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1523,
		"Locality_Name": "All India Institute Of Local Self-government",
		"Latitude": "19.07008908",
		"Longitude": "72.84985936",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1524,
		"Locality_Name": "Government Polytechnic Mumbai",
		"Latitude": "19.0636571",
		"Longitude": "72.84601497",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1525,
		"Locality_Name": "Mahatma Gandhi Vidyamandir",
		"Latitude": "19.06307662",
		"Longitude": "72.84987208",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1526,
		"Locality_Name": "Asian Paints",
		"Latitude": "19.07683263",
		"Longitude": "72.85059263",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1527,
		"Locality_Name": "Centaur House",
		"Latitude": "19.07582593",
		"Longitude": "72.8499526",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1528,
		"Locality_Name": "Mudra House",
		"Latitude": "19.07593221",
		"Longitude": "72.85171927",
		"Station": {
			"id": 19
		}
	},
	{
		"id": 1530,
		"Locality_Name": "Kalpataru Synergy",
		"Latitude": "19.07637025",
		"Longitude": "72.85083447",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1531,
		"Locality_Name": "MCGM H- East Ward Office",
		"Latitude": "19.08523696",
		"Longitude": "72.84458018",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1532,
		"Locality_Name": "Panbai International School",
		"Latitude": "19.08570829",
		"Longitude": "72.84518584",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1533,
		"Locality_Name": "Mumbai University Gate No.2",
		"Latitude": "19.07424474",
		"Longitude": "72.85254781",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1534,
		"Locality_Name": "Yes Bank House",
		"Latitude": "19.08314262",
		"Longitude": "72.84549069",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1535,
		"Locality_Name": "Datta Mandir Vakola",
		"Latitude": "19.08350899",
		"Longitude": "72.85261742",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1536,
		"Locality_Name": "Pejawar Mutt",
		"Latitude": "19.08540459",
		"Longitude": "72.84369861",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1537,
		"Locality_Name": "Santacruz Gymkhana",
		"Latitude": "19.07878553",
		"Longitude": "72.84451265",
		"Station": {
			"id": 20
		}
	},
	{
		"id": 1538,
		"Locality_Name": "Utkarsh Mandal Hall",
		"Latitude": "19.1011049",
		"Longitude": "72.85214698",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1539,
		"Locality_Name": "Vile Parle Police Station",
		"Latitude": "19.09637478",
		"Longitude": "72.85561605",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1540,
		"Locality_Name": "Hotel Ginger",
		"Latitude": "19.09737139",
		"Longitude": "72.85401429",
		"Station": {
			"id": 21
		}
	},
	{
		"id": 1541,
		"Locality_Name": "Air cargo complex",
		"Latitude": "19.09650404",
		"Longitude": "72.86569924",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1542,
		"Locality_Name": "Ascot center",
		"Latitude": "19.10493499",
		"Longitude": "72.8710001",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1543,
		"Locality_Name": "Hiranandani Fulcrum",
		"Latitude": "19.10418535072566",
		"Longitude": "72.87205804334876",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1544,
		"Locality_Name": "Star Hub",
		"Latitude": "19.10604128",
		"Longitude": "72.86852067",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1545,
		"Locality_Name": "Air Traffic Control Complex",
		"Latitude": "19.09674275",
		"Longitude": "72.86345172",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1546,
		"Locality_Name": "Sahar Police Station",
		"Latitude": "19.10012998",
		"Longitude": "72.87017208",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1547,
		"Locality_Name": "Aurika by lemon Tree House",
		"Latitude": "19.10387204",
		"Longitude": "72.86305538",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1548,
		"Locality_Name": "Hotel Suba International",
		"Latitude": "19.10651113",
		"Longitude": "72.86027698",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1549,
		"Locality_Name": "Our Lady Of Health School",
		"Latitude": "19.09958785",
		"Longitude": "72.86598495",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1550,
		"Locality_Name": "Our Lady Of Health Church",
		"Latitude": "19.09932425",
		"Longitude": "72.86644629",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1551,
		"Locality_Name": "Shri Munisuvrat Shwetambar Jain Derasar, JB Nagar",
		"Latitude": "19.10875803",
		"Longitude": "72.86779758",
		"Station": {
			"id": 22
		}
	},
	{
		"id": 1552,
		"Locality_Name": "Ascot Centre",
		"Latitude": "19.10486884",
		"Longitude": "72.87138668",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1553,
		"Locality_Name": "Crescent Business Park",
		"Latitude": "19.10006027",
		"Longitude": "72.88149852",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1554,
		"Locality_Name": "Hiranandani Fulcrum",
		"Latitude": "19.10418535072566",
		"Longitude": "72.87205804334876",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1555,
		"Locality_Name": "Oberoi Flight Services",
		"Latitude": "19.10604363",
		"Longitude": "72.87387859",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1556,
		"Locality_Name": "The Qube",
		"Latitude": "19.102641",
		"Longitude": "72.87977146",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1557,
		"Locality_Name": "Star Hub",
		"Latitude": "19.10612998",
		"Longitude": "72.86936725",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1558,
		"Locality_Name": "Ambassador Hotel",
		"Latitude": "19.10374327",
		"Longitude": "72.8755212",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1559,
		"Locality_Name": "Fairfield by Marriott",
		"Latitude": "19.10058338",
		"Longitude": "72.88236012",
		"Station": {
			"id": 23
		}
	},
	{
		"id": 1560,
		"Locality_Name": "Antariksh - Thakoor House",
		"Latitude": "19.1100847",
		"Longitude": "72.88190025",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1561,
		"Locality_Name": "Leela Business Park",
		"Latitude": "19.11100507",
		"Longitude": "72.87415985",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1562,
		"Locality_Name": "Raheja Platinum",
		"Latitude": "19.10903082",
		"Longitude": "72.88553258",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1563,
		"Locality_Name": "Skyline Icon",
		"Latitude": "19.10575366",
		"Longitude": "72.88140419",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1564,
		"Locality_Name": "Times Square",
		"Latitude": "19.10791779",
		"Longitude": "72.88378063",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1565,
		"Locality_Name": "Vaman Centre",
		"Latitude": "19.11152358",
		"Longitude": "72.88231116",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1567,
		"Locality_Name": "Hotel Lemon Tree Premier",
		"Latitude": "19.10770826",
		"Longitude": "72.88221163",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1568,
		"Locality_Name": "Hotel Novotel",
		"Latitude": "19.11035707",
		"Longitude": "72.87584692",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1569,
		"Locality_Name": "Hind Saurashtra Industrial Estate",
		"Latitude": "19.10685566",
		"Longitude": "72.88197271",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1570,
		"Locality_Name": "Mittal Industrial Estate",
		"Latitude": "19.10407258",
		"Longitude": "72.88217542",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1571,
		"Locality_Name": "Saifee Masjid Marol",
		"Latitude": "19.11407486",
		"Longitude": "72.87613394",
		"Station": {
			"id": 24
		}
	},
	{
		"id": 1572,
		"Locality_Name": "Kalpataru Square",
		"Latitude": "19.11258373",
		"Longitude": "72.87153195",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1573,
		"Locality_Name": "Options Primo",
		"Latitude": "19.12046948",
		"Longitude": "72.87621922",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1574,
		"Locality_Name": "Sahar Plaza",
		"Latitude": "19.11289742",
		"Longitude": "72.86869303",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1575,
		"Locality_Name": "Samruddhi Venture Park",
		"Latitude": "19.1206764",
		"Longitude": "72.87058829",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1577,
		"Locality_Name": "MIDC Police Station",
		"Latitude": "19.1177391",
		"Longitude": "72.86832105",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1579,
		"Locality_Name": "ESIC Hospital",
		"Latitude": "19.11852603",
		"Longitude": "72.86737131",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1580,
		"Locality_Name": "New Empire Industrial Estate",
		"Latitude": "19.11401032",
		"Longitude": "72.8710547",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1581,
		"Locality_Name": "Marol Education Academy's\nHigh School & Junior College",
		"Latitude": "19.11922058",
		"Longitude": "72.88155504",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1582,
		"Locality_Name": "IBL House - IndusInd Bank",
		"Latitude": "19.11414585",
		"Longitude": "72.86786047",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1583,
		"Locality_Name": "Rolta Tower One",
		"Latitude": "19.12134387",
		"Longitude": "72.87129985",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1584,
		"Locality_Name": "St.Vincent Pallotti Church",
		"Latitude": "19.12103014",
		"Longitude": "72.88106013",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1585,
		"Locality_Name": "Maheshwari Nagar Society",
		"Latitude": "19.11663843",
		"Longitude": "72.87392048",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1586,
		"Locality_Name": "Sterling Court",
		"Latitude": "19.11641707",
		"Longitude": "72.8731477",
		"Station": {
			"id": 25
		}
	},
	{
		"id": 1587,
		"Locality_Name": "74 Techno Park",
		"Latitude": "19.12187645",
		"Longitude": "72.87268417",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1588,
		"Locality_Name": "Seepz Gate No 1",
		"Latitude": "19.12450008",
		"Longitude": "72.87222372",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1589,
		"Locality_Name": "Seepz Gate No 2",
		"Latitude": "19.12199027",
		"Longitude": "72.87333716",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1590,
		"Locality_Name": "Seepz Gate No 3",
		"Latitude": "19.12972111",
		"Longitude": "72.87761869",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1591,
		"Locality_Name": "Western Religious Power committee",
		"Latitude": "19.12818483",
		"Longitude": "72.87447154",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1592,
		"Locality_Name": "Mahakali Caves",
		"Latitude": "19.1302521",
		"Longitude": "72.87318452",
		"Station": {
			"id": 26
		}
	},
	{
		"id": 1593,
		"Locality_Name": "Aarey JVLR Depot",
		"Latitude": "19.13366652",
		"Longitude": "72.88316518",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1594,
		"Locality_Name": "Aarey JVLR Depot Gate 1",
		"Latitude": "19.13498332",
		"Longitude": "72.88245522",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1595,
		"Locality_Name": "Aarey JVLR Depot Gate 2",
		"Latitude": "19.13392584",
		"Longitude": "72.88725577",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1596,
		"Locality_Name": "Ganesh Nagar",
		"Latitude": "19.13278874",
		"Longitude": "72.88000692",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1597,
		"Locality_Name": "Sariput Nagar",
		"Latitude": "19.1316292",
		"Longitude": "72.87592556",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1598,
		"Locality_Name": "Kamal Amrohi Studio",
		"Latitude": "19.13472092",
		"Longitude": "72.87684456",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1599,
		"Locality_Name": "Modern Bakery",
		"Latitude": "19.13940217",
		"Longitude": "72.87678446",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1600,
		"Locality_Name": "Aarey Colony",
		"Latitude": "19.13762065",
		"Longitude": "72.88230351",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1601,
		"Locality_Name": "Milind Nagar",
		"Latitude": "19.12851275",
		"Longitude": "72.88870635",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1602,
		"Locality_Name": "Manohar Nagar",
		"Latitude": "19.1267181",
		"Longitude": "72.88958094",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1603,
		"Locality_Name": "Shiv Shakti Nagar",
		"Latitude": "19.12211332",
		"Longitude": "72.89016663",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1604,
		"Locality_Name": "National Security Guard",
		"Latitude": "19.12850189",
		"Longitude": "72.88690991",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1605,
		"Locality_Name": "Vijay Nagar",
		"Latitude": "19.12112074",
		"Longitude": "72.87887507",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1606,
		"Locality_Name": "Mahakali Caves",
		"Latitude": "19.13020931",
		"Longitude": "72.8735411",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1607,
		"Locality_Name": "Petrol Pump",
		"Latitude": "19.12900551",
		"Longitude": "72.88222547",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1608,
		"Locality_Name": "SEEPZ Gate 3",
		"Latitude": "19.129562",
		"Longitude": "72.87770472",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1609,
		"Locality_Name": "Western Regional Test Laborator",
		"Latitude": "19.12629589",
		"Longitude": "72.87349664",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1610,
		"Locality_Name": "State Bank Of India",
		"Latitude": "19.12673501",
		"Longitude": "72.87720427",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1611,
		"Locality_Name": "Punjab National Bank",
		"Latitude": "19.12678828",
		"Longitude": "72.87684892",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1612,
		"Locality_Name": "Central Bank Of India",
		"Latitude": "19.12517671",
		"Longitude": "72.87347648",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1613,
		"Locality_Name": "Maroleshwar Mahadev Temple",
		"Latitude": "19.12436784",
		"Longitude": "72.88138983",
		"Station": {
			"id": 27
		}
	},
	{
		"id": 1614,
		"Locality_Name": "Ram Temple",
		"Latitude": "19.12559305",
		"Longitude": "72.87934271",
		"Station": {
			"id": 27
		}
	}
]
# Convert to GeoJSON
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [item["Longitude"], item["Latitude"]]
            },
            "properties": {
                k: v for k, v in item.items() if k not in ["Latitude", "Longitude"]
            }
        }
        for item in data
    ]
}




# Output as JSON string
print(json.dumps(geojson, indent=2))

# Save to a .geojson file
with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, indent=2)

print("GeoJSON file saved as output.geojson")