# Contenido de la demo Hotel Abelay (Palma) (es/ca/en/fr). Hechos de hotelabelay.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación individual','Habitación doble','Habitación triple'],'ca':['Habitació individual','Habitació doble','Habitació triple'],'en':['Single room','Double room','Triple room'],'fr':['Chambre individuelle','Chambre double','Chambre triple']}
RD={
'es':['Para 1 persona, con wifi gratuito, televisión, aire acondicionado y calefacción, gel, champú, sábanas y toallas.','Para 2 personas, con baño privado, wifi gratuito, televisión y aire acondicionado con bomba de calor.','Para 3 personas, con el mismo equipamiento: wifi gratuito, televisión, climatización y baño privado.'],
'ca':['Per a 1 persona, amb wifi gratuït, televisió, aire condicionat i calefacció, gel, xampú, llençols i tovalloles.','Per a 2 persones, amb bany privat, wifi gratuït, televisió i aire condicionat amb bomba de calor.','Per a 3 persones, amb el mateix equipament: wifi gratuït, televisió, climatització i bany privat.'],
'en':['For 1 person, with free wifi, TV, air conditioning and heating, shower gel, shampoo, sheets and towels.','For 2 people, with private bathroom, free wifi, TV and heat-pump air conditioning.','For 3 people, with the same equipment: free wifi, TV, air conditioning and private bathroom.'],
'fr':['Pour 1 personne, avec wifi gratuit, télévision, climatisation et chauffage, gel douche, shampooing, draps et serviettes.','Pour 2 personnes, avec salle de bain privée, wifi gratuit, télévision et climatisation par pompe à chaleur.','Pour 3 personnes, avec le même équipement : wifi gratuit, télévision, climatisation et salle de bain privée.']}
ART={
'hero':('waves',9401,['#1f5a6b','#f3c58a','#f9e3bf','#2f7387','#1f5a6b','#133a46']),
'intro':('skyline',9402,['#1f5a6b','#e8a865','#f7d8a5','#1c5262','#174452','#0f2f39']),
'r1':('columns',9411,['#edf1f2','#f6f8f9','#c4793c','#1f5a6b','#133a46']),
'r2':('arches',9412,['#f2ebe0','#e5bf8d','#c27238','#1f5a6b','#133a46']),
'r3':('hills',9413,['#e6eef0','#f2ecd6','#f0c27f','#a9c2a4','#7fa28a','#567a68']),
'g1':('waves',9421,['#235f71','#f0c184','#f7e0b9','#33788c','#235f71','#153e4a']),
'g2':('columns',9422,['#ebeff1','#f5f7f8','#c1763a','#1f5a6b','#133a46']),
'g3':('skyline',9423,['#1f5a6b','#e6a561','#f6d6a1','#1b505f','#16424f','#0e2d37']),
'g4':('arches',9424,['#f1e9dd','#e2bb88','#bf6f35','#1f5a6b','#133a46']),
'g5':('hills',9425,['#e4ecef','#f0e9d2','#eebf7b','#a6bf9f','#7c9f86','#537764']),
'g6':('waves',9426,['#1d5767','#efbe80','#f6ddb5','#2d7084','#1d5767','#123843'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Abelay · Hotel familiar cerca de la Plaza de España, Palma',see_rooms='Ver habitaciones',hero_k='Palma · Mallorca',hero_t='Un hotel familiar a pocos minutos de la Plaza de España',hero_s='Confortable y acogedor, con 55 habitaciones reformadas y recepción 24 horas en el centro de Palma.',
 intro_t='Bien situado para recorrer la isla',intro_p1='Cerca de las piscinas municipales de Son Hugo, el conservatorio, la plaza de toros y el casco antiguo.',
 intro_p2='A 2 minutos hay una parada de autobuses y a 10 minutos el Parc de Les Estacions, la estación intermodal para moverse por toda Mallorca.',
 stats=['55 habitaciones','Recepción 24 horas','Wifi gratis','Gimnasio'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individuales, dobles y triples, reformadas entre 2017 y 2020.',
 svcs=['Recepción 24 horas','Cafetería, bar y restaurante','Gimnasio','Wifi gratuito','Ascensor','Accesible para movilidad reducida','Parking bajo petición','Consigna de equipajes'],
 loc_p='Carrer de Pablo Iglesias 49 · 07004 Palma, Illes Balears. A unos 15 minutos en coche del aeropuerto.',
 chips=['¿Qué habitaciones tiene?','¿Dónde está?','¿Qué servicios tiene?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Abelay · Hotel familiar a prop de la Plaça d\'Espanya, Palma',see_rooms='Veure habitacions',hero_k='Palma · Mallorca',hero_t='Un hotel familiar a pocs minuts de la Plaça d\'Espanya',hero_s='Confortable i acollidor, amb 55 habitacions reformades i recepció 24 hores al centre de Palma.',
 intro_t='Ben situat per recórrer l\'illa',intro_p1='A prop de les piscines municipals de Son Hugo, el conservatori, la plaça de toros i el nucli antic.',
 intro_p2='A 2 minuts hi ha una parada d\'autobusos i a 10 minuts el Parc de Les Estacions, l\'estació intermodal per moure\'s per tot Mallorca.',
 stats=['55 habitacions','Recepció 24 hores','Wifi gratis','Gimnàs'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individuals, dobles i triples, reformades entre 2017 i 2020.',
 svcs=['Recepció 24 hores','Cafeteria, bar i restaurant','Gimnàs','Wifi gratuït','Ascensor','Accessible per a mobilitat reduïda','Pàrquing sota petició','Consigna d\'equipatges'],
 loc_p='Carrer de Pablo Iglesias 49 · 07004 Palma, Illes Balears. A uns 15 minuts amb cotxe de l\'aeroport.',
 chips=['Quines habitacions té?','On és?','Quins serveis té?','Com es reserva?']),
'en':dict(title='Hotel Abelay · Family hotel near Plaza de España, Palma',see_rooms='See the rooms',hero_k='Palma · Mallorca',hero_t='A family hotel a few minutes from Plaza de España',hero_s='Comfortable and welcoming, with 55 refurbished rooms and a 24-hour reception in central Palma.',
 intro_t='Well placed to explore the island',intro_p1='Close to the Son Hugo municipal pools, the conservatory, the bullring and the old town.',
 intro_p2='A bus stop is 2 minutes away and Parc de Les Estacions, the intermodal station for getting around Mallorca, 10 minutes away.',
 stats=['55 rooms','24-hour reception','Free wifi','Gym'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Singles, doubles and triples, refurbished between 2017 and 2020.',
 svcs=['24-hour reception','Café, bar and restaurant','Gym','Free wifi','Lift','Accessible for reduced mobility','Parking on request','Luggage storage'],
 loc_p='Carrer de Pablo Iglesias 49 · 07004 Palma, Illes Balears. About 15 minutes by car from the airport.',
 chips=['What rooms does it have?','Where is it?','What services are there?','How do I book?']),
'fr':dict(title='Hotel Abelay · Hôtel familial près de la Plaza de España, Palma',see_rooms='Voir les chambres',hero_k='Palma · Majorque',hero_t='Un hôtel familial à quelques minutes de la Plaza de España',hero_s='Confortable et accueillant, avec 55 chambres rénovées et une réception 24 h/24 au centre de Palma.',
 intro_t='Bien situé pour parcourir l\'île',intro_p1='Près des piscines municipales de Son Hugo, du conservatoire, des arènes et de la vieille ville.',
 intro_p2='Un arrêt de bus est à 2 minutes et le Parc de Les Estacions, la gare intermodale pour circuler dans tout Majorque, à 10 minutes.',
 stats=['55 chambres','Réception 24 h/24','Wifi gratuit','Salle de sport'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelles, doubles et triples, rénovées entre 2017 et 2020.',
 svcs=['Réception 24 h/24','Cafétéria, bar et restaurant','Salle de sport','Wifi gratuit','Ascenseur','Accessible aux personnes à mobilité réduite','Parking sur demande','Consigne à bagages'],
 loc_p='Carrer de Pablo Iglesias 49 · 07004 Palma, Illes Balears. À environ 15 minutes en voiture de l\'aéroport.',
 chips=['Quelles chambres a-t-il ?','Où est-il ?','Quels services propose-t-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RU='https://www.hotelabelay.es/be/rv.xhtml?lng='
BOOK=dict(mode='engine',url={'es':RU+'es','ca':RU+'es','en':RU+'en','fr':RU+'fr'})
D=dict(name='Hotel Abelay',ac='#1f5a6b',ac2='#c27238',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='Carrer de Pablo Iglesias 49 · 07004 Palma',phones=['+34 971 75 60 34'],emails=['info@hotelabelay.es'],maps='Hotel Abelay, Carrer de Pablo Iglesias 49, Palma',t=T)
META=dict(repo='demo-hotel-abelay-palma',name='Hotel Abelay',legal_name='Abelay, S.L.',registry_ids=['CIF B07304389','Registro Mercantil de Illes Balears, tomo 1970, folio 28'],
 url='https://www.hotelabelay.es/es/home.html',domain='hotelabelay.es',municipality='Palma',province='Illes Balears',sector='hotel familiar de 55 habitaciones cerca de la Plaza de España de Palma',
 read_at='2026-10-29T13:12:00+01:00',created_at='2026-10-29T13:10:00+01:00',built_at='2026-10-29T13:25:00+01:00',audit_date='2026-10-29T13:03:54+01:00',
 rating=dict(value=4.3,coincide=['web','direccion'],date='2026-10-29T10:35:01+01:00',url='https://www.google.com/maps/place/HOTEL+ABELAY/@39.5828438,2.6549636,17z/data=!4m9!3m8!1s0x129792ff1f84d851:0x939d629ecb34ee3a!5m2!4m1!1i2!8m2!3d39.5828438!4d2.6549636!16s%2Fg%2F1tf1303h'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hotel (/be/rv.xhtml, el destino de sus botones «Reservar»); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Dónde está?','K03'),('¿Cómo llego desde el aeropuerto?','K04'),('¿Hay transporte público cerca?','K05'),('¿Qué servicios tiene?','K06'),('¿Hay parking?','K07'),('¿La recepción abre 24 horas?','K08'),('¿Tienen cuna?','K09'),('¿Cómo reservo?','K10'),('¿Quién es el titular?','K11'),('¿Se puede fumar?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Hay piscina en el hotel?',None),('¿Admiten mascotas?',None)],
'ca':[('Quines habitacions té?','K01'),('Què tenen les habitacions?','K02'),('On és?','K03'),('Com hi arribo des de l\'aeroport?','K04'),('Hi ha transport públic a prop?','K05'),('Quins serveis té?','K06'),('Hi ha pàrquing?','K07'),('La recepció obre 24 hores?','K08'),('Teniu bressol?','K09'),('Com reservo?','K10'),('Qui és el titular?','K11'),('Es pot fumar?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Hi ha piscina a l\'hotel?',None),('Admeteu mascotes?',None)],
'en':[('What rooms does it have?','K01'),('What do the rooms have?','K02'),('Where is it?','K03'),('How do I get there from the airport?','K04'),('Is there public transport nearby?','K05'),('What services are there?','K06'),('Is there parking?','K07'),('Is the reception open 24 hours?','K08'),('Do you have a cot?','K09'),('How do I book?','K10'),('Who is the owner?','K11'),('Can I smoke?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Is there a swimming pool at the hotel?',None),('Are pets allowed?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Qu\'ont les chambres ?','K02'),('Où est-il ?','K03'),('Comment venir depuis l\'aéroport ?','K04'),('Y a-t-il des transports publics à proximité ?','K05'),('Quels services propose-t-il ?','K06'),('Y a-t-il un parking ?','K07'),('La réception est-elle ouverte 24 heures ?','K08'),('Avez-vous un lit bébé ?','K09'),('Comment réserver ?','K10'),('Qui est le titulaire ?','K11'),('Peut-on fumer ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Y a-t-il une piscine à l\'hôtel ?',None),('Les animaux sont-ils admis ?',None)]}
