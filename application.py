
import numpy as np
import pandas as pd
import pickle
import streamlit as st


Companies=['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Fiat', 'Datsun', 'Jeep',
       'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen', 'BMW',
       'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo',
       'Kia', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel', 'Peugeot']


Models=['Maruti Swift Dzire', 'Skoda Rapid 1.5', 'Honda City 2017-2020',
       'Hyundai i20 Sportz', 'Maruti Swift VXI', 'Hyundai Xcent 1.2',
       'Maruti Wagon R', 'Maruti 800 DX', 'Toyota Etios VXD',
       'Ford Figo Diesel', 'Renault Duster 110PS', 'Maruti Zen LX',
       'Maruti Swift 1.3', 'Mahindra KUV 100', 'Maruti Ertiga SHVS',
       'Hyundai i20 1.4', 'Maruti Alto LX', 'Hyundai i20 2015-2017',
       'Mahindra Verito 1.5', 'Honda WR-V i-DTEC', 'Maruti SX4 ZDI',
       'Tata Tigor 2017-2020', 'Maruti Baleno Delta', 'Maruti Alto 800',
       'Chevrolet Enjoy TCDi', 'Maruti Omni E', 'Maruti Vitara Brezza',
       'Fiat Palio 1.2', 'Maruti Omni 8', 'Hyundai i20 1.2',
       'Maruti Alto K10', 'Hyundai Verna VTVT', 'Datsun GO D',
       'Tata Safari DICOR', 'Maruti 800 Std', 'Jeep Compass 1.4',
       'Honda City i', 'Honda City V', 'Toyota Fortuner 4x4',
       'Toyota Innova 2.5', 'Mercedes-Benz B Class', 'Honda Amaze S',
       'Mitsubishi Pajero Sport', 'Maruti Ciaz Zeta', 'Honda Jazz VX',
       'Toyota Innova Crysta', 'Audi A6 2.0', 'Toyota Corolla Altis',
       'Mercedes-Benz New C-Class', 'Tata Manza ELAN',
       'Hyundai i10 Magna', 'Hyundai i20 Asta', 'Ford Figo 1.2P',
       'Volkswagen Ameo 1.5', 'Maruti Swift VDI', 'Maruti Swift Star',
       'Maruti Ertiga ZXI', 'Tata Indica DLS', 'Volkswagen Vento Diesel',
       'Ford EcoSport 1.5', 'BMW X1 sDrive20i', 'Maruti Celerio ZXI',
       'Datsun GO A', 'Hyundai i10 Era', 'Volkswagen Polo 1.2',
       'Volkswagen Vento Petrol', 'Maruti Zen Estilo', 'Tata Manza Aura',
       'Maruti Eeco 7', 'Maruti Baleno Zeta', 'Mahindra Scorpio VLX',
       'Ford Freestyle Titanium', 'Volkswagen Passat 1.8',
       'Tata Indica Vista', 'Mahindra XUV500 W11', 'Tata Indigo CS',
       'Hyundai Verna 1.6', 'Hyundai i20 Magna', 'Maruti Celerio VXI',
       'Nissan Terrano XL', 'Hyundai Creta 1.6', 'Renault KWID 1.0',
       'Maruti Alto LXi', 'Maruti Ertiga VDI', 'Hyundai Santro Xing',
       'Audi Q5 35TDI', 'Lexus ES 300h', 'Jaguar XF 2.0',
       'Jeep Wrangler 2016-2019', 'Land Rover Discovery',
       'Mercedes-Benz S-Class S', 'BMW 5 Series', 'BMW X1 sDrive',
       'BMW X4 M', 'Skoda Superb LK', 'Mercedes-Benz E-Class E250',
       'MG Hector Sharp', 'Honda City i-VTEC', 'Volvo XC40 D4',
       'Audi Q7 35', 'Maruti Ciaz ZDi', 'Hyundai Elantra S',
       'Jaguar XE 2016-2019', 'Tata Nexon 1.2', 'Hyundai Elantra SX',
       'Skoda Rapid 1.6', 'Mercedes-Benz CLA 200', 'Toyota Glanza V',
       'Tata Nexon 1.5', 'BMW 3 Series', 'Toyota Camry 2.5',
       'Toyota Camry W4', 'Maruti Ertiga BSIV', 'Volvo XC90 T8',
       'Ford Figo Aspire', 'Maruti Ritz VDi', 'Hyundai Grand i10',
       'Volkswagen Ameo 1.0', 'Honda City 1.5', 'Daewoo Matiz SD',
       'Toyota Fortuner 4x2', 'Tata Zest Quadrajet', 'Maruti Zen LXI',
       'Hyundai Verna Transform', 'Hyundai Getz GLS', 'Hyundai Elite i20',
       'Maruti Ciaz 1.3', 'Tata Tigor 1.2', 'Toyota Etios GD',
       'Honda Brio S', 'Tata Hexa XE', 'Maruti Baleno Alpha',
       'Tata Safari Storme', 'Renault KWID RXT', 'Datsun GO T',
       'Tata Zest Revotron', 'Nissan Sunny XL', 'Nissan Micra Active',
       'Mahindra Ssangyong Rexton', 'Mahindra Quanto C8',
       'Maruti Ritz LDi', 'Mahindra XUV500 W4', 'Maruti Eeco 5',
       'Hyundai Accent GLE', 'Mahindra XUV500 W8', 'Hyundai i10 Sportz',
       'Hyundai Getz 1.3', 'Maruti Swift LXI', 'Maruti Ignis 1.3',
       'Tata Hexa XTA', 'Mahindra Marazzo M6', 'Toyota Fortuner 3.0',
       'Tata Tiago 1.05', 'Mahindra Thar CRDe', 'Maruti Swift 1.2',
       'Mahindra Scorpio LX', 'Tata Sumo Gold', 'Tata Tiago Wizz',
       'Honda Brio Exclusive', 'Tata Manza Club', 'Tata New Safari',
       'Mahindra Bolero SLE', 'Mahindra Bolero DI',
       'Mercedes-Benz GL-Class 220d', 'Mahindra Bolero 2011-2019',
       'Hyundai i20 Active', 'Maruti Alto LXI', 'Chevrolet Beat LS',
       'Honda City i-DTEC', 'Maruti Ertiga VXI', 'Nissan Terrano XV',
       'Mahindra Willys CJ', 'Renault KWID RXL', 'Hyundai Creta 1.4',
       'Tata Tiago 1.2', 'Maruti Swift ZXI', 'Maruti Celerio LXI',
       'Nissan Micra Diesel', 'Maruti A-Star Vxi', 'Maruti Swift Ldi',
       'Mahindra XUV300 W8', 'Toyota Fortuner 2.8', 'Honda Brio 1.2',
       'Volkswagen Ameo 1.2', 'Nissan Sunny XV', 'Toyota Etios Liva',
       'Renault Duster 85PS', 'Tata Nano STD', 'Volkswagen GTI 1.8',
       'Maruti Swift AMT', 'Toyota Etios VX', 'Honda Amaze V',
       'Volvo V40 D3', 'Honda CR-V 2.4L', 'Maruti SX4 Celebration',
       'Hyundai Verna XXi', 'Hyundai Verna CRDi', 'Tata Indigo LS',
       'Maruti Eeco CNG', 'Mahindra XUV500 AT', 'Hyundai EON Sportz',
       'Maruti Eeco Smiles', 'Hyundai Xcent 1.1', 'Maruti 800 AC',
       'Volkswagen Polo 1.5', 'Tata Hexa XT', 'Datsun RediGO 1.0',
       'Chevrolet Enjoy 1.3', 'Maruti SX4 S', 'Chevrolet Captiva LT',
       'Ford Fiesta Titanium', 'Kia Seltos HTE', 'Maruti Celerio LDi',
       'Honda Civic 1.8', 'Chevrolet Beat Diesel', 'Ford Figo Petrol',
       'Tata Indica V2', 'Datsun RediGO S', 'Hyundai EON Era',
       'Chevrolet Beat LT', 'Chevrolet Sail 1.2', 'Jeep Compass 2.0',
       'Tata Venture EX', 'Hyundai EON Magna', 'Maruti Estilo LXI',
       'Hyundai Getz GLX', 'Ford Classic 1.4', 'Mahindra Bolero SLX',
       'Honda Jazz 1.2', 'Honda BR-V i-VTEC', 'Hyundai Verna S',
       'Nissan Micra XV', 'Datsun RediGO T', 'Hyundai Santro Sportz',
       'Maruti Ertiga ZDI', 'Mahindra Scorpio 1.99', 'Honda Amaze VX',
       'Ford Ecosport 1.5', 'Tata Aria Pride', 'Tata Sumo CX',
       'Mahindra TUV 300', 'Tata Tiago NRG', 'Tata Bolt Revotron',
       'Honda Accord V6', 'Mahindra Scorpio S10', 'Tata Bolt Quadrajet',
       'Mahindra Xylo E4', 'Maruti A-Star Zxi', 'Hyundai i10 Asta',
       'Fiat Grande Punto', 'Hyundai Getz 1.5',
       'Maruti S-Cross 2017-2020', 'Toyota Yaris V',
       'Nissan Sunny Diesel', 'Mahindra Xylo D2', 'Maruti Swift Vdi',
       'Mahindra Xylo E6', 'Tata Nano Cx', 'Chevrolet Tavera Neo',
       'Mahindra Scorpio M2DI', 'Honda CR-V 2.4', 'Datsun GO Anniversary',
       'Mahindra Bolero PLUS', 'Nissan Sunny XE', 'Skoda Rapid Ultima',
       'Mahindra XUV500 W10', 'Mahindra Bolero GLX', 'Tata Indigo eCS',
       'Mahindra Scorpio 2.6', 'Hyundai EON D', 'Volkswagen Polo Diesel',
       'Fiat Linea 1.3', 'Mahindra Xylo D4', 'Honda Amaze i-VTEC',
       'Mahindra Scorpio S2', 'Hyundai Santro GLS', 'Skoda Superb 1.8',
       'Ford Endeavour Hurricane', 'Ford Freestyle Trend',
       'Chevrolet Aveo U-VA', 'Datsun RediGO Sport',
       'Mahindra Bolero ZLX', 'Mahindra XUV500 W6', 'Datsun GO Plus',
       'Mahindra Bolero VLX', 'Maruti Alto Std', 'Honda Amaze E',
       'Mahindra Verito Vibe', 'Tata Sumo GX', 'Maruti Ritz ZXi',
       'Ford Fiesta 1.4', 'Mahindra Scorpio SLE', 'Hyundai EON 1.0',
       'Tata Indigo GLX', 'Chevrolet Sail Hatchback', 'Maruti Esteem Vxi',
       'Tata Tigor 1.05', 'Tata Manza Aqua', 'Mahindra Xylo H4',
       'Ford Fiesta Classic', 'Renault Triber RXT',
       'Mahindra Scorpio Getaway', 'Hyundai Accent GLX',
       'Ford Fusion 1.4', 'Skoda Octavia Ambition', 'Audi A4 2.0',
       'Maruti XL6 Alpha', 'Hyundai Santro Magna', 'Maruti Zen D',
       'Renault Triber RXZ', 'Mahindra Scorpio 2009-2014',
       'Hyundai Elantra CRDi', 'Hyundai Santa Fe', 'Mahindra Thar DI',
       'Chevrolet Spark 1.0', 'Mahindra Scorpio S4', 'Mahindra Xylo E8',
       'Mahindra Scorpio EX', 'Hyundai Verna Xi', 'Ford Aspire Titanium',
       'Ford Figo Titanium', 'Fiat Punto 1.3', 'Ford Fiesta EXi',
       'Chevrolet Optra Magnum', 'Tata Sumo MKII', 'Honda Mobilio S',
       'Toyota Qualis Fleet', 'Honda BRV i-VTEC', 'Honda Jazz V',
       'BMW X6 xDrive30d', 'Chevrolet Cruze LTZ',
       'Mercedes-Benz GLA Class', 'Kia Seltos HTX', 'Maruti Ciaz RS',
       'BMW 6 Series', 'Chevrolet Sail LT', 'Mahindra NuvoSport N8',
       'Maruti Swift VVT', 'Renault Scala Diesel', 'Maruti Omni BSIII',
       'Maruti SX4 Vxi', 'Renault KWID Climber', 'Mahindra Jeep Classic',
       'Tata Nano CX', 'Mahindra Verito 1.4', 'Chevrolet Optra 1.6',
       'Maruti Ciaz Alpha', 'Maruti Omni MPI', 'Hyundai i20 Era',
       'Hyundai Getz GLE', 'Maruti Ciaz VDi', 'Maruti Swift Glam',
       'Renault Lodgy World', 'Honda BRV i-DTEC', 'Tata Indigo CR4',
       'Maruti Ritz VXI', 'Renault Pulse RxZ', 'Honda Accord 2.4',
       'Chevrolet Sail 1.3', 'Maruti Swift ZDi', 'Hyundai Verna 1.4',
       'Hyundai Santro GS', 'Nissan Terrano XE', 'Mahindra Supro LX',
       'Maruti Celerio VDi', 'Ford Ecosport 1.0', 'Mahindra Ingenio CRDe',
       'Maruti Swift LDI', 'Tata Tiago XT', 'Mahindra Bolero B2',
       'Maruti Ignis 1.2', 'Fiat Linea Emotion', 'Audi Q5 2.0',
       'Tata Nano XTA', 'Hyundai Sonata CRDi', 'Mahindra Jeep CL',
       'Honda Jazz 1.5', 'BMW X1 sDrive20d', 'Maruti Swift ZDI',
       'Mahindra Bolero B4', 'Ford Ecosport Sports', 'Mahindra Quanto C4',
       'Mahindra XUV500 W7', 'Maruti Zen VXi', 'Fiat Linea Classic',
       'Honda BR-V i-DTEC', 'Maruti Swift DDiS', 'Ford Endeavour 3.2',
       'Mahindra Renault Logan', 'Maruti Ciaz VXi', 'Maruti Ritz VXi',
       'Datsun RediGO A', 'Nissan Kicks XV', 'Maruti SX4 VDI',
       'Nissan Micra XL', 'Renault Duster Adventure', 'Maruti SX4 ZXI',
       'Mahindra Scorpio S11', 'Honda Civic Hybrid',
       'Volkswagen Vento 1.6', 'Volkswagen Jetta 2.0L',
       'Volkswagen Vento 1.5', 'Mercedes-Benz M-Class ML',
       'Volkswagen Polo 2015-2019', 'Mahindra Marazzo M8',
       'Honda Mobilio V', 'Mahindra Scorpio VLS', 'Honda WR-V i-VTEC',
       'Mitsubishi Pajero 2.8', 'Ford Figo 1.5D', 'Tata Indigo LX',
       'Volkswagen Polo Petrol', 'Maruti Ciaz AT', 'Renault Duster 4x4',
       'Mahindra Jeep MM', 'Mercedes-Benz E-Class E270',
       'Mahindra Quanto C2', 'Tata Indigo V', 'Ford Endeavour 3.0L',
       'Volkswagen Jetta 1.6', 'Ford Figo 1.5P', 'Nissan Teana XL',
       'Skoda Yeti Ambition', 'Maruti Ciaz S', 'Hyundai Accent VIVA',
       'Hyundai Accent CRDi', 'Mahindra Bolero Power',
       'Mahindra Scorpio Intelli', 'Jaguar XF 2.2',
       'Honda City Corporate', 'Audi Q3 2.0', 'Honda Civic ZX',
       'Hyundai Santro Asta', 'Force Gurkha Hard', 'Mahindra Marazzo M2',
       'Skoda Octavia Style', 'Mahindra Logan Diesel',
       'Honda Jazz Select', 'Volkswagen Polo GT', 'Ford Endeavour 2.5L',
       'Tata Indigo GLS', 'Hyundai Santro LP', 'Maruti Ertiga 1.5',
       'Maruti Celerio ZDi', 'Maruti Zen Base', 'Tata Sumo EX',
       'Tata Hexa XM', 'Mahindra Bolero XL', 'Mahindra XUV500 W9',
       'Audi A3 35', 'Maruti Ciaz Delta', 'Audi Q5 3.0', 'Audi Q7 3.0',
       'Mahindra Scorpio S3', 'Land Rover Freelander', 'Daewoo Matiz SS',
       'Maruti Celerio X', 'Honda City E', 'Chevrolet Aveo 1.4',
       'Tata Aria Pure', 'Maruti Ciaz 1.4', 'Mahindra XUV300 W6',
       'Maruti Dzire VXI', 'Volkswagen Vento IPL', 'Ford Ikon 1.3',
       'Toyota Qualis GS', 'Ford Ikon 1.4', 'Toyota Etios V',
       'Hyundai Accent Executive', 'Maruti SX4 Zxi', 'Maruti Zen LXi',
       'Maruti Omni 5', 'Nissan Kicks XL', 'Mahindra Quanto C6',
       'Toyota Etios Cross', 'Mahindra Scorpio S7', 'Ford Aspire Trend',
       'Honda Brio V', 'Maruti Baleno LXI', 'Chevrolet Captiva 2.2',
       'Ford Ikon 1.6', 'Tata Nano LX', 'Ford Fiesta Diesel',
       'Ford Fusion Plus', 'Tata Nano Lx', 'Maruti Omni LPG',
       'Ford Classic 1.6', 'Toyota Etios Diesel', 'Renault Fluence 1.5',
       'Honda City VX', 'Toyota Corolla AE', 'Tata Xenon XT',
       'Hyundai Santro Era', 'Force One SX', 'Honda Mobilio RS',
       'Ford Fiesta 1.6', 'BMW 7 Series', 'Maruti Dzire LXI',
       'Maruti 800 EX', 'Mahindra Xylo H9', 'Jaguar XF 3.0', 'Audi Q3 35',
       'Maruti Celerio VXi', 'Volvo S60 D4', 'Tata Nano Twist',
       'Hyundai Elantra GT', 'Hyundai Elantra GLS', 'Volvo V40 Cross',
       'Mitsubishi Lancer 2.0', 'BMW X7 xDrive', 'Skoda Superb Elegance',
       'Toyota Premio Base', 'Skoda Fabia 1.2', 'Mahindra XUV500 W5',
       'Volkswagen Jetta 2.0', 'Honda Brio E', 'Ford Endeavour 4x2',
       'Audi A4 35', 'Nissan Micra Fashion', 'Toyota Platinum Etios',
       'Mahindra Bolero LX', 'Maruti Swift LXi', 'Renault Captur 1.5',
       'Mercedes-Benz GL-Class 350', 'Maruti Baleno Sigma',
       'Skoda Fabia 1.4', 'Renault Fluence Diesel', 'Maruti Gypsy King',
       'Tata Estate Std', 'Mahindra Scorpio Gateway', 'Maruti Alto STD',
       'Toyota Etios G', 'Renault Koleos 2.0', 'Renault Lodgy 85PS',
       'Ambassador CLASSIC 1500', 'Tata Harrier XZ', 'Ford Fiesta 1.5',
       'Tata Indigo TDI', 'Volkswagen Multivan TDI',
       'Mercedes-Benz E-Class E', 'Nissan Micra XE', 'Hyundai Accent GLS',
       'Fiat Punto 1.2', 'Fiat Avventura Power', 'Skoda Laura Ambiente',
       'Hyundai Getz 1.1', 'Mahindra Verito 1.6', 'Tata Indica GLS',
       'Chevrolet Enjoy Petrol', 'Tata Nano XE', 'Chevrolet Tavera B3',
       'Toyota Camry V4', 'Maruti Ritz LXi', 'Toyota Etios 1.5',
       'Chevrolet Tavera LS', 'Hyundai Sonata 2.4', 'Ford EcoSport S',
       'Maruti Esteem LX', 'Fiat Punto Pure', 'Hyundai Santro LE',
       'Maruti A-Star Lxi', 'Renault Pulse RxL', 'Toyota Fortuner 2.5',
       'Fiat Avventura MULTIJET', 'Ashok Leyland Stile',
       'Hyundai EON LPG', 'Mahindra Scorpio SLX', 'Tata Sumo SE',
       'Skoda Fabia 1.2L', 'Toyota Glanza G', 'Tata Indigo Grand',
       'Tata Aria Prestige', 'Chevrolet Tavera B1-10', 'Isuzu MUX 2WD',
       'MG Hector Smart', 'Audi A4 1.8', 'Toyota Etios VD',
       'Opel Astra 1.6', 'Skoda Octavia Classic',
       'Skoda Octavia Elegance', 'Hyundai Tucson 2.0', 'Renault KWID AMT',
       'Volkswagen Passat 2.0', 'Volkswagen Polo 1.0',
       'Hyundai Accent DLS', 'Maruti Esteem DI', 'Renault Lodgy Stepway',
       'Maruti Swift VXi', 'Maruti Ciaz VDI', 'Tata Winger Deluxe',
       'Maruti Ertiga LXI', 'Skoda Fabia Scout', 'Honda Amaze SX',
       'Maruti Ritz LXI', 'Force One EX', 'Ambassador Classic 2000',
       'Skoda Octavia RS', 'Audi Q5 45', 'Jaguar XF Diesel',
       'Hyundai Sonata 2.4L', 'Toyota Corolla H2', 'Honda City 1.3',
       'Tata Venture LX', 'Maruti 800 Uniq', 'Maruti Omni CNG',
       'Audi A6 35', 'Ambassador Grand 1500', 'Maruti Baleno RS',
       'Mahindra Logan Petrol', 'Toyota Qualis FS', 'Maruti Ignis Zeta',
       'Maruti Omni Limited', 'Tata Spacio Gold-10/6',
       'Mahindra Scorpio 2006-2009', 'Honda Accord VTi-L',
       'Maruti Ciaz ZXi', 'Mercedes-Benz E-Class Exclusive',
       'Hyundai Venue SX', 'Maruti SX4 Green', 'Volkswagen CrossPolo 1.5',
       'Renault Duster Petrol', 'Maruti Esteem Lxi', 'Skoda Octavia L',
       'Honda City S', 'Hyundai i20 Petrol', 'Tata Tiago 2019-2020',
       'Hyundai Verna SX', 'Chevrolet Enjoy 1.4', 'Maruti Swift VDi',
       'Mahindra Marshal DI', 'Volkswagen Vento Konekt',
       'Skoda Kodiaq 2.0', 'Volkswagen Passat Highline',
       'Renault Duster RXL', 'Hyundai Santro AT', 'Tata Indica DLX',
       'Toyota Etios 1.4', 'Hyundai Santro DX', 'Maruti Esteem AX',
       'Skoda Octavia Ambiente', 'Maruti Ritz ZDi', 'Isuzu D-Max V-Cross',
       'Toyota Corolla DX', 'Mahindra Bolero Pik-Up',
       'Mercedes-Benz E-Class E350', 'Honda Jazz Basic',
       'BMW X3 xDrive20d', 'Datsun RediGO SV', 'Datsun RediGO AMT',
       'Skoda Rapid Monte', 'Toyota Land Cruiser', 'Hyundai i10 LPG',
       'Hyundai i20 Diesel', 'Maruti Zen VXI', 'Hyundai Santro LS',
       'Maruti Alto AX', 'Ford Endeavour 2.2', 'Maruti Zen Std',
       'Volkswagen Polo Select', 'BMW X5 3.0d', 'Tata Aria Pleasure',
       'Ford Ikon 1.8', 'Honda Amaze Anniversary', 'Fiat Punto EVO',
       'Land Rover Range', 'Peugeot 309 GLD', 'Honda Amaze EX',
       'Maruti Ertiga LDI', 'Renault KWID RXE', 'Hyundai Tucson CRDi',
       'Maruti Swift Lxi', 'Mahindra Thar 4X4', 'Maruti Dzire ZXI',
       'Honda CR-V 2.0L', 'Maruti Ritz Genus', 'Skoda Octavia Rider',
       'Tata Indigo VS', 'Maruti Alto Green', 'Chevrolet Trailblazer LTZ',
       'Isuzu MU 7', 'Mercedes-Benz GLC 220d', 'Hyundai Sonata 2.0L',
       'Hyundai Accent Gvs', 'Volvo XC60 Inscription',
       'Chevrolet Tavera B2', 'Mahindra Scorpio S5', 'Maruti Zen Classic',
       'Ford Figo 1.5', 'Ambassador Grand 2000', 'Volvo S90 D4',
       'Maruti S-Presso VXI', 'Renault Fluence 2.0', 'Renault Duster RXZ',
       'Audi A3 40', 'Honda City ZXi', 'Chevrolet Cruze LT']

Fuel_type=['Diesel', 'Petrol', 'LPG', 'CNG']

trans=['Manual', 'Automatic']


own=['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner']

sellers=['Individual', 'Dealer', 'Trustmark Dealer']

seat=[1,2,3,4,5,6,7,8,9,10]


pipe=pickle.load(open('prediction.pkl','rb'))

header=st.container()
with header:
    st.title("Used Car Price Predictor")


car_companies = st.selectbox('Select The Car Company', sorted(Companies))

car_model = st.selectbox('Select The Car model', sorted(Models))

col1,col2=st.columns(2)

with col1:
    Year=st.number_input('Year')

with col2:
    Km_driven=st.number_input('Kilometers Driven')


col3,col4=st.columns(2)

with col3:
    Fuel=st.selectbox('Select The Fuel Type',sorted(Fuel_type))

with col4:
    Transmission=st.selectbox('Select The Car Transmission',sorted(trans))

col5,col6=st.columns(2)

with col5:
    Owner=st.selectbox('Select The Owner Type',sorted(own))

with col6:
    Seller=st.selectbox('Select The Seller',sorted(sellers))

col7,col8,col9=st.columns(3)

with col7:
    seats=st.selectbox('Select The number of seats',(seat))

with col8:
    Mileage=st.number_input('Mileage')

with col9:
    Engine=st.number_input('Engine')


if st.button('Predict'):

    company=car_companies
    name=car_model
    year=Year
    Km_Driven=Km_driven
    fuel_type=Fuel
    transmission=Transmission
    owner=Owner
    seller_type=Seller
    seat=seats
    mileage=Mileage
    engine=Engine

    input=pd.DataFrame({'company':[company],'name':[name],'year':[year],'km_driven':[Km_Driven],'fuel':[fuel_type],'seller_type':[seller_type],'transmission':[transmission],'owner':[owner],'mileage':[mileage],'engine':[engine],'seats':[seat]})

    result=pipe.predict(input)
    price=result[0]

    st.header('Price : '+str(round(price,2))+' Rs')