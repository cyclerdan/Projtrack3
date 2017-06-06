# This doesn't even pretend to work yet.

import sqlite3

def populate():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    departments = ['Mathematics', 'Computer Science', 'CTLE', 'History', 'Student', 'ISP', 'KSOM', 'Recreation',
                   'Counseling', 'Philosophy', 'OIM', 'Physics', 'Biology', 'Nursing', 'English', 'Criminal Justice',
                   'Theology', 'Athletics', 'Physical Therapy', 'FAC', 'Psychology', 'Multicultural Affairs',
                   'Foreign Languages', 'Education', 'Communication', 'HAHR', 'Annual Given Programs',
                   'Human Resources', 'Exercise Science', 'Occupational Therapy', 'Student Affairs', 'Library', 'PCPS',
                   'Chemistry', 'HADM', 'World Languages and Culture', 'Public Safety', 'Accounting', 'Management',
                   'Art & History', 'Wellness Center', 'Business', 'Career Services']

    for obj in departments:
        add_department(c, obj)

    clients = [['Aileen', 'McHale', 'aileen.mchale@scranton.edu', 'CTLE'],
               ['Betsey', 'Moylan', 'Betsey.moylan@scranton.edu', 'FAC'],
               ['Brian', 'Snapp', 'brian.snapp@scranton.edu', 'CTLE'],
               ['Patrick', 'Mohr', 'jpatrick.mohr@scranton.edu', 'Philosophy'],
               ['Shannon', 'Sennefelder', 'shannon.sennefelder@scranton.edu', 'Student'],
               ['Ileana', 'Syzmanski ', 'Ileana.syzmanski@scranton.edu', 'Philosophy'],
               ['Sharon', 'Hudacek', 'Sharon.Hudacek@scranton.edu', 'Nursing'],
               ['Paula', 'Semenza', 'paula.semenza@scranton.edu', 'CTLE'],
               ['Jane ', 'Alperin', 'janeleslie.alperin@scranton.edu', 'KSOM'],
               ['Mary Ellen', 'Pichiarello ', 'MaryEllen.pichiarello@scranton.edu', 'CTLE'],
               ['Harold', 'Anderson', 'harold.anderson@scranton.edu', 'HAHR'],
               ['Ileana', 'Szymanski', 'ileana.szymanski@scranton.edu', 'Philosophy'],
               ['Scott', 'Breloff', 'scott.breloff@scranton.edu', 'Exercise Science'],
               ['Liz', 'Pililero', 'elizabeth.piliero@scranton.edu', 'Student'],
               ['Dona', 'Carpenter ', 'Dona.Carpenter@scranton.edu', 'Nursing'],
               ['Charles', 'Kratz', 'charles.kratz@scranton.edu', 'Student Affairs'],
               ['Rebecca', 'Mikesell', 'rebecca.mikesell@scranton.edu', 'Communication'],
               ['TY', 'Rippon', 'Tyler.Rippon@scranton.edu', 'Student Affairs'],
               ['Margaret', 'Snare', 'margaret.snare@scranton.edu', 'Student'],
               ['David', 'Linhares', 'david.linhares@scranton.edu', 'PCPS'],
               ['Ise', 'Kannebecker', 'ise.kannebecker@scranton.edu', 'Occupational Therapy'],
               ['Edmund', 'Kosmahl', 'edmund.kosmahl@scranton.edu', 'Physical Therapy'],
               ['Ashley', 'Allegra', 'ashley.allegra@scranton.edu', 'Student'],
               ['Nicole', 'Ward', 'nicole.ward@scranton.edu', 'Student'],
               ['John', 'Sanko', 'john.sanko@scranton.edu', 'Physical Therapy'],
               ['Danielle ', 'Colaprico ', 'Danielle.Colaprico@scranton.edu', 'Occupational Therapy'],
               ['Bonnie ', 'Oldham', 'Bonnie.Oldham@scranton.edu', 'Annual Given Programs'],
               ['Alyson', 'Aitken', 'alyson.aitken@scranton.edu', 'Student'],
               ['Len', 'Tischler', 'len.tischler@scranton.edu', 'KSOM'],
               ['Kaitlin', 'Delpriora', 'kaitlin.delpriora@scranton.edu', 'Student'],
               ['Katie', 'Delpriora', 'kaitlin.delpriora@scranton.edu', 'Occupational Therapy'],
               ['Caitlyn ', 'Keeler ', 'caitlyn.keeler@scranton.edu', 'Occupational Therapy'],
               ['Vicki', 'Fierro', 'victoria.fierro@scranton.edu', 'Occupational Therapy'],
               ['Kait', 'Sullivan', 'kaitlyn.sullivan@scranton.edu', 'Student'],
               ['Christopher', 'Baumann', 'christopher.baumann@scranton.edu', 'Chemistry'],
               ['Michael ', 'Carey', 'michael.carey@scranton.edu', 'Biology'],
               ['Natalia', 'Juscinska', 'natalia.juscinska@scranton.edu', 'Student'],
               ['Joe', 'Vinson', 'joe.vinson@scranton.edu', 'Chemistry'],
               ['Lee', 'Penyak', 'lee.penyak@scranton.edu', 'History'],
               ['Sean', 'Brennan', 'sean.brennan@scranton.edu', 'History'],
               ['Robert', 'Smith', 'robert.smith@scranton.edu', 'Biology'],
               ['Cynthia', 'Cann', 'cynthia.cann@scranton.edu', 'KSOM'],
               ['Mary Beth', 'Holmes ', 'marybeth.holmes@scranton.edu', 'Communication'],
               ['John', 'Conway', 'john.conway@scranton.edu', 'Biology'],
               ['David', 'Morgan', 'david.morgan@scranton.edu', 'Chemistry'],
               ['Riaz', 'Hussain', 'riaz.hussain@scranton.edu', 'KSOM'],
               ['Maria', 'Squire', 'maria.squire@scranton.edu', 'Biology'],
               ['Michael', 'Cann', 'michael.cann@scranton.edu', 'Chemistry'],
               ['Andrew', 'LaZella', 'andrew.lazella@scranton.edu', 'Philosophy'],
               ['Cyrus', 'Olsen', 'cyrus.olsen@scranton.edu', 'Theology'],
               ['Mary', 'Goldschmidt', 'mary.goldschmidt@scranton.edu', 'CTLE'],
               ['Harold', 'Anderson', 'harold.anderson@scranton.edu', 'HADM'],
               ['Rob', 'McKeage', 'robert.mckeage@scranton.edu', 'Management'],
               ['Amye ', 'Archer', 'amye.archer@scranton.edu', 'CTLE'],
               ['Jan', 'Hall', 'Jan.hall@scranton.edu', 'Annual Given Programs'],
               ['Hans', 'Patel', 'hanskamal.patel@scranton.edu', 'Student'],
               ['David', 'Friedrichs', 'david.friedrichs@scranton.edu', 'Criminal Justice'],
               ['Mary Elaine', 'Southard', 'maryelaine.southard@scranton.edu', 'Nursing'],
               ['Elizabeth', 'Eckley', 'elizabeth.eckley@scranton.edu', 'Criminal Justice'],
               ['Majed', 'Albaridi', 'majed.albaridi@scranton.edu', 'CTLE'],
               ['David', 'Gallick', 'david.gallick@scranton.edu', 'Counseling'],
               ['Jamie ', 'Trnka', 'jamie.trnka@scranton.edu', 'World Languages and Culture'],
               ['Maria', 'Virbitsky', 'virbitsky.maria@scranton.edu', 'Annual Given Programs'],
               ['Stacy', 'Smulowitz', 'stacy.smulowitz@scranton.edu', 'Annual Given Programs'],
               ['Laura ', 'VanVokenburg', 'laura.vanvolkenburg@scranton.edu', 'Occupational Therapy'],
               ['Margarete', 'Zalon', 'Margarete.Zalon@scranton.edu', 'Nursing'],
               ['Jennifer', 'Voorman', 'Jennifer.Voorman@scranton.edu', 'Occupational Therapy'],
               ['Jan', 'Kelly', 'jan.kelly@scranton.edu', 'Communication'],
               ['Derek', 'Drasba', 'derek.drasba@scranton.edu', 'Occupational Therapy'],
               ['Kimberly Feucht', 'Feucht', 'kimberly.feucht@scranton.edu', 'Annual Given Programs'],
               ['Adam', 'Pratt', 'adam.pratt@scranton.edu', 'Annual Given Programs'],
               ['Josephine', 'Dunn', 'Josephine.Dunn@scranton.edu', 'Annual Given Programs'],
               ['Eugeniu', 'Grigorescu', 'eugeniu.grigorescu@scranton.edu', 'CTLE'],
               ['Declan', 'Mulhall', 'declan.mulhall@scranton.edu', 'Physics'],
               ['Rohdeena', 'Hudson', 'rohdeena.hudson@scranton.edu', 'Student'],
               ['Marlene ', 'Morgan', 'marlene.morgan@scranton.edu', 'Occupational Therapy'],
               ['Kelly', 'Babinski', 'kelly.babinski@scranton.edu', 'Student'],
               ['Vincent', 'Yanusaskas ', 'vincent.vanusaskas@scranton.edu', 'Student Affairs'],
               ['Stephen', 'Mansour', 'stephen.mansour@scranton.edu', 'KSOM'],
               ['Michael', 'Friedman', 'michael.friedman@scranton.edu', 'English'],
               ['Xiong', 'Zhongcheng', 'zhongcheng.xiong@scranton.edu', 'Mathematics'],
               ['George', 'Gomez', 'george.gomez@scranton.edu', 'Annual Given Programs'],
               ['Patricia ', 'Wisniewski', 'patricia.wisniewski@scranton.edu', 'Annual Given Programs'],
               ['Denise', 'Karpowicz', 'denise.karpowicz@scranton.edu', 'CTLE'],
               ['Patrick', 'Clark', 'Patrick.clark@scranton.edu', 'Annual Given Programs'],
               ['Jeremy', 'Brees', 'jeremy.brees@scranton.edu', 'KSOM'],
               ['Andrew', 'Gregorowicz', 'andrew.gregorowicz@scranton.edu', 'KSOM'],
               ['Himana', 'Patel', 'himana.patel@scranton.edu', 'CTLE'],
               ['Kellia', 'Giambrone', 'kellia.giambrone@scranton.edu', 'Student'],
               ['Maragret', 'Hogan', 'margaret.hogan@scranton.edu', 'Philosophy'],
               ['Dana', 'Maida', 'dana.maida@scranton.edu', 'Physical Therapy'],
               ['Mary', 'Theroux', 'mary.theroux@scranton.edu', 'Nursing'],
               ['Bonnie', 'Xiong', 'bx@desirelearn.scranton.edu', 'Annual Given Programs'],
               ['Christel', 'Hornstra', 'christel.hornstra@scranton.edu', 'Annual Given Programs'],
               ['Sheli', 'McHugh', 'michelle.mchugh@scranton.edu', 'Student Affairs'],
               ['Eric', 'Plumer', 'eric.plumer@scranton.edu', 'Theology'],
               ['Donald', 'Bergmann', 'donald.bergmann@scranton.edu', 'Public Safety'],
               ['Harry', 'Dammer', 'Harry.Dammer@scranton.edu', 'Criminal Justice'],
               ['Robert', 'Handloff', 'robert.handloff@scranton.edu', 'History'],
               ['Denise', 'Jacoby-Smith', 'denise.jacobysmith@scranton.edu', 'Annual Given Programs'],
               ['Ashley', 'Dudinyak', 'ashley.dudinyak@scranton.edu', 'Annual Given Programs'],
               ['Jennifer', 'Pennington', 'jennifer.pennington@scranton.edu', 'CTLE'],
               ['Bob', 'Liskowioz', 'bob.liskowioz@scranton.edu', 'CTLE'],
               ['Satya', 'Chattopadhay', 'Satya.Chattopadhay@scranton.edu', 'Annual Given Programs'],
               ['Kim', 'Wheeler', 'kim.wheeler@scranton.edu', 'Annual Given Programs'],
               ['Iordinas', 'Petsas', 'Iordinas.petsas@scranton.edu', 'KSOM'],
               ['David', 'Angeloni', 'david.angeloni@scranton.edu', 'Education'],
               ['Julie', 'Nastasi', 'Julie.nastasi@scranton.edu', 'Occupational Therapy'],
               ['Kevin', 'Wilkerson', 'kevin.wilkerson@scranton.edu', 'Counseling'],
               ['Marian', 'Farell', 'marian.farell@scranton.edu', 'Nursing'],
               ['Dan', 'Haggerty', 'daniel.haggerty@scranton.edu', 'Philosophy'],
               ['James', 'Boyle', 'james.boyle@scranton.edu', 'Accounting'],
               ['Kimberly', 'Pavlick', 'kimberly.pavlick@scranton.edu', 'Communication'],
               ['Tara', 'Fay', 'Tara.Fay@scranton.edu', 'Biology'],
               ['Catherine', 'Lovecchio', 'Catherine.Lovecchio@scranton.edu', 'Nursing'],
               ['Robert', 'Spalletta', 'robert.spalletta@scranton.edu', 'Physics'],
               ['Masood', 'Otarod', 'masood.otarod@scranton.edu', 'Mathematics'],
               ['Julie', 'Lartz', 'julie.lartz@scranton.edu', 'English'],
               ['Sultan', 'Sirwi', 'sultan.sirwi@scranton.edu', 'Student'],
               ['Bob', 'Spinelli', 'bob.spinelli@scranton.edu', 'Accounting'],
               ['Tata ', 'Mbugua', 'Tata.Mbugua@scranton.edu', 'Education'],
               ['Shuhua', 'Fan', 'shuhua.fan@scranton.edu', 'History'],
               ['Lee Ann', 'Eschbach', 'leeann.eschbach@scranton.edu', 'Counseling'],
               ['Brian', 'Carpenter', 'brian.carpenter@scranton.edu', 'Accounting'],
               ['Rick', 'Malloy', 'rick.malloy@scranton.edu', 'Theology'],
               ['Mary Jane', 'DiMattio', 'maryjane.dimattio@scranton.edu', 'Nursing'],
               ['Ann', 'Culp', 'ann.culp@scranton.edu', 'Nursing'],
               ['Janice', 'Voltzow', 'janice.voltzow@scranton.edu', 'Biology'],
               ['Ann Marie', 'Cittadino', 'ann-marie.cittadino@scranton.edu', 'Biology'],
               ['Linda', 'Smith', 'linda.smith@scranton.edu', 'Theology'],
               ['Bob', 'Parsons', 'robert.parsons@scranton.edu', 'Foreign Languages'],
               ['Ann', 'Feeney', 'ann.feeney@scranton.edu', 'Nursing'],
               ['Linda', 'Lewis', 'linda.lewis@scranton.edu', 'Nursing'],
               ['John', 'Sivalon', 'john.sivalon@scranton.edu', 'Theology'],
               ['Nathan', 'Lefler', 'nathan.lefler@scranton.edu', 'Theology'],
               ['Carol', 'Reinson', 'carol.reinson@scranton.edu', 'Nursing'],
               ['Susan', ' Scandall', 'susan.scandall@scranton.edu', 'Nursing'],
               ['Teresa', 'Grettano', 'teresa.grettano@scranton.edu', 'English'],
               ['Darla', 'Miller-Lanning', 'darlene.miller-lanning@scranton.edu', 'Art & History'],
               ['Richard', 'Molloy', 'richard.molloy@scranton.edu', 'Theology'],
               ['Jim', 'Boyle', 'james.boyle@scranton.edu', 'Accounting'],
               ['Christos', 'Pargianas', 'christos.pargianas@scranton.edu', 'KSOM'],
               ['Jennifer', 'Cutsforth', 'Jennifer.Cutsforth@scranton.edu', 'Accounting'],
               ['Andreas', 'Christopher', 'Andreas.Christopher@scranton.edu', 'Accounting'],
               ['John', 'Kranick', 'john.kranick@scranton.edu', 'Student'],
               ['Dan', 'Haggerty', 'daniel.haggerty@scranton.edu', 'Annual Given Programs'],
               ['Tracey', 'Collins', 'tracey.collins@scranton.edu', 'Physical Therapy'],
               ['Raymond', 'Schwenk', 'raymond.schwenk@scranton.edu', 'PCPS'],
               ['Jennifer', 'Custafano', 'Jennifer.Custafano@scranton.edu', 'CTLE'],
               ['John', 'Ruddy', 'john.ruddy@scranton.edu', 'Accounting'],
               ['Verna', 'Eschenfelder', 'verna.eschenfelder@scranton.edu', 'Physical Therapy'],
               ['Parry', 'Koslow', 'parry.koslow@scranton.edu', 'Accounting'],
               ['Daphne', 'Golden', 'daphne.golden@scranton.edu', 'Physical Therapy'],
               ['Huey Shi', 'Chew ', 'hueyshi.chew@scranton.edu', 'Multicultural Affairs'],
               ['Cristen', 'Walker ', 'cristen.walker@scranton.edu', 'Nursing'],
               ['Dona', 'Bauman', 'dona.bauman@scranton.edu', 'Nursing'],
               ['William ', 'Rowe', 'william.rowe@scranton.edu', 'Philosophy'],
               ['Joan', 'Davis', 'joan.davis@scranton.edu', 'English'],
               ['Danielle', 'Arigo', 'danielle.arigo@scranton.edu', 'Psychology'],
               ['Michael ', 'Hardisky', 'michael.hardisky@scranton.edu', 'Biology'],
               ['Deborah', 'Longest', 'deborah.longest@scranton.edu', 'Nursing'],
               ['Lawrence', 'Kennedy', 'lawrence.kennedy@scranton.edu', 'History'],
               ['Jessica', 'Bachman', 'jessica.bachman@scranton.edu', 'Exercise Science'],
               ['Mary', 'Rafter', 'mary.rafter@scranton.edu', 'Philosophy'],
               ['Blank', 'Blank', 'Blank', 'Mathematics'],
               ['Christine', 'Zakzewski', 'christine.zakzewski@scranton.edu', 'Physics'],
               ['Richard ', 'Hennigan', 'richard.hennigan@scranton.edu', 'Nursing'],
               ['James', 'Buchanan', 'james.buchanan@scranton.edu', 'Psychology'],
               ['Rebecca', 'Dalgin', 'Rebecca.Dalgin@scranton.edu', 'Counseling'],
               ['Stacey ', 'Smulowitz ', 'Stacey.Smulowitz@scranton.edu', 'Communication'],
               ['Michael', 'Costello', 'michael.costello@scranton.edu', 'Management'],
               ['Arielle', 'Burkavage', 'arielle.burkavage@scranton.edu', 'Biology'],
               ['Marilyn', 'Highhouse', 'marilyn.highhouse@scranton.edu', 'Nursing'],
               ['Nancy', 'Cummings', 'nancy.cummings@scranton.edu', 'Accounting'],
               ['Amy', 'Szydlowski', 'szydla@gmail.com', 'HADM'],
               ['Thomas', 'Pesci', 'thomas.pesci@scranton.edu', 'Accounting'],
               ['Jill', 'Warker', 'jill.warker@scranton.edu', 'Accounting'],
               ['Charles', 'Pinches', 'charles.pinches@scranton.edu', 'Theology'],
               ['Tim', 'Holland', 'tim.holland@scranton.edu', 'History'],
               ['Antoinette', 'Glover', 'antoinette.glover@scranton.edu', 'Accounting'],
               ['Gary', 'Kwiecinski', 'Gary.Kwiecinski@scranton.edu', 'Biology'],
               ['Delia', 'Sumrall', 'Delia.sumrall@scranton.edu', 'KSOM'],
               ['Julia', 'Guzman', 'julia.guzman@scranton.edu', 'Occupational Therapy'],
               ['Roger ', 'Lloyd', 'roger.lloyd@scranton.edu', 'Mathematics'],
               ['Allison', 'Lai', 'allison.lai@scranton.edu', 'CTLE'],
               ['Alex', 'Pinarreta', 'alex.pinarreta@scranton.edu', 'Annual Given Programs'],
               ['Raquel', 'Biondi', 'raquel.biondi@scranton.edu', 'Accounting'],
               ['Bernie', 'Gilligan', 'bernard.gilligan@scranton.edu', 'Nursing'],
               ['Clay', 'Nottleman', 'clay.nottleman@scranton.edu', 'Human Resources'],
               ['sultain', 'sirui', 'sultain.sirui@scranton.edu', 'CTLE'],
               ['Samuel ', 'Lesko', 'samuel.lesko@scranton.edu', 'HADM'],
               ['Scott', 'Reilly', 'scott.reilly@scranton.edu', 'Education'],
               ['Robert', 'Parsons', 'robert.parsons@scranton.edu', 'Foreign Languages'],
               ['Charles', 'Lenns', 'charles.lenns@scranton.edu', 'Accounting'],
               ['Joseph', 'Kraus', 'joseph.kraus@scranton.edu', 'English'],
               ['Jennifer ', 'Schwartz', 'jennifer.schwartz@scranton.edu', 'Physical Therapy'],
               ['Rebecca', 'Serafin', 'rebecca.serafin@scranton.edu', 'Accounting'],
               ['Paul', 'Cutrufello', 'paul.cutrufello@scranton.edu', 'Exercise Science'],
               ['deborah', 'miller', 'deborah.miller@scranton.edu', 'Physical Therapy'],
               ['Satyanarayana', 'Prattipati', 'Satyanarayana.Prattipati@scranton.edu', 'KSOM'],
               ['Andree', 'Catalfamo', 'andree.catalfamo@scranton.edu', 'Accounting'],
               ['Jill', 'Lear', 'jill.lear@scranton.edu', 'Nursing'],
               ['Ross', 'Diane', 'ross.diane@scranton.edu', 'Nursing'],
               ['Elizabeth', 'Rozelle', 'elizabeth.rozelle@scranton.edu', 'Accounting'],
               ['Christine', 'Talenti', 'christine.talenti@scranton.edu', 'Accounting'],
               ['Mary Anne', 'Foley', 'maryanne.foley@scranton.edu', 'Theology'],
               ['Elisa', 'Grave', 'elisa.garve@scranton.edu', 'Occupational Therapy'],
               ['Kristin', 'Leccese', 'N/A@scranton.edu', 'Occupational Therapy'],
               ['Amy', 'Golden', 'Amy.Golden@scranton.edu', 'Nursing'],
               ['Lisa', 'Kozden', 'lisa.kozden@scranton.edu', 'Occupational Therapy'],
               ['Sandy', 'Pesavento', 'sandy.pesavento@scranton.edu', 'Accounting'],
               ['William ', 'Lambert', 'william.lambert@scranton.edu', 'Occupational Therapy'],
               ['Sandy', 'Pesavento', 'sandy.pesavento@scranton.edu', 'Counseling'],
               ['Mary', 'Goldschmidt', 'mary.goldschmidt@scranton.edu', 'CTLE'],
               ['Rodeen', 'Lechleitner', 'Rodeen.Lechleitner@scranton.edu', 'PCPS'],
               ['Doug', 'Boyle', 'doug.boyle@scranton.edu', 'Accounting'],
               ['vincent', 'castellani', 'vincent.castellani@scranton.edu', 'KSOM'],
               ['Luke', 'Vitagliano', 'luke.vitagliano@scranton.edu', 'Counseling'],
               ['Hanna', 'Sandor', 'hanna.sandor@scranton.edu', 'Nursing'],
               ['Alex', 'Ochalski', 'alex.ochalski@scranton.edu', 'Student'],
               ['Sarah', 'Novak', 'sarah.novak@scranton.edu', 'Student'],
               ['Lisa ', 'Lesneski', 'Lisa.lesneski@scranton.edu', 'Nursing'],
               ['Brigid ', 'Frein', 'brigid.frein@scranton.edu', 'Theology'],
               ['Mathew', 'Lasewicz', 'mathew.lasewicz@scranton.edu', 'Student'],
               ['Julie', 'Brackeva-Phillips', 'julie.brackeva-phillips@scranton.edu', 'CTLE'],
               ['Joan', 'Grossman', 'joan.grossman@scranton.edu', 'Accounting'],
               ['Susan ', 'Scanland', 'susan.scanland@scratnon.edu', 'Accounting'],
               ['Anthony', 'Marasco', 'anthony.marasco@scranton.edu', 'CTLE'],
               ['Jinghan', 'Cai', 'jinghan.cai@scranton.edu', 'KSOM'],
               ['Vincent', 'Marshall', 'vincent.marshall@scranton.edu', 'Accounting'],
               ['Kyle', 'Hassett', 'kyle.hassett@scranton.edu', 'CTLE'],
               ['Blaise', 'Casillo', 'blaise.casillo@scranton.edu', 'CTLE'],
               ['Vincent', 'Rocco', 'vincent.rocco@scranton.edu', 'KSOM'],
               ['richard', 'trygar', 'richard.trygar@scranton.edu', 'Chemistry'],
               ['Sabreen', 'Aljeddani', 'sabreen.aljeddani@scranton.edu', 'Student'],
               ['Herbert', 'Hauser', 'herbert.hauser@scranton.edu', 'Psychology'],
               ['Jean', 'Lenville', 'jean.lenville@scranton.edu', 'Student Affairs'],
               ['Gretchen', 'Welby', 'gretchen.welby@scranton.edu', 'Biology'],
               ['Virginia', 'ticchietti', 'virginia.ticchietti@scranton.edu', 'World Languages and Culture'],
               ['Willis', 'Conover', 'willis.conover@scranton.edu', 'History'],
               ['Susan', 'Boafo-Arthur', 'susan.boafo-arthur@scranton.edu', 'Counseling'],
               ['Patricia', 'Popeck', 'patricia.popeck@scranton.edu', 'Wellness Center'],
               ['Arthur', 'Catino', 'arthur.catino@scranton.edu', 'Chemistry'],
               ['John ', 'Sivalon', 'John.Sivalon@scranton.edu', 'Accounting'],
               ['Maria', 'Johnson', 'maria.johnson@scranton.edu', 'Theology'],
               ['Stephen', 'Mansour', 'stephen.mansour@scranton.edu', 'Accounting'],
               ['Julian', 'Liest', 'julian.liest@scranton.edu', 'Career Services'],
               ['Beth', 'O''Neil', 'beth.oneil@scranton.edu', 'Theology'],
               ['Mary Jane', 'Hanson', 'maryjane.hanson@scranton.edu', 'Accounting'],
               ['Abhijit', 'Roy', 'abhijit.roy@scranton.edu', 'Accounting'],
               ['Arthur ', 'Catino', 'Arthur.Catino@scranton.edu', 'Chemistry'],
               ['Barbara', 'Buxton', 'barabara.buxton@scranton.edu', 'Nursing'],
               ['Paula', 'Roe-Prior', 'paula.roe-prior@scranton.edu', 'HADM'],
               ['Terri Freeman', 'Smith', 'terrifreeman.smith@scranton.edu', 'Human Resources'],
               ['Laura', 'Skoronski', 'laura.skoronski@scranton.edu', 'Nursing'],
               ['Oliver', 'Morgan', 'oliver.morgan@scranton.edu', 'Counseling'],
               ['Joseph', 'Gnall', 'joseph.gnall@scranton.edu', 'Computer Science'],
               ['Joan', 'Grossman', 'joan.grossman@scranton.edu', 'Exercise Science'],
               ['David', 'Dzurec', 'david.dzurec@scranton.edu', 'History'],
               ['Kenneth', 'Carroll', 'kenneth.carroll@scranton.edu', 'Student'],
               ['Kim', 'Paulsen', 'kim.paulsen@scranton.edu', 'CTLE'],
               ['Jennifer', 'Kaschak', 'jennifer.kaschak@scranton.edu', 'Education'],
               ['Irene', 'Goll', 'irene.goll@scranton.edu', 'KSOM'],
               ['Sean', 'Batzel', 'sean.batzel@scranton.edu', 'Computer Science'],
               ['John', 'Norocross', 'john.norcross@scranton.edu', 'Psychology'],
               ['Autumn', 'Kearney', 'autumn.kearney@scranton.edu', 'Art & History'],
               ['Barry', 'Kuhle', 'barry.kuhle@scranton.edu', 'Psychology'],
               ['Melissa', 'Starace', 'melissa.starace@scranton.edu', 'Management'],
               ['Courtney', 'Lancia', 'courtney.lancia@scranton.edu', 'Accounting'],
               ['Will', 'Cohen', 'will.cohen@scranton.edu', 'Accounting'],
               ['Craig', 'Gallagher', 'craig.gallagher@scranton.edu', 'Business'],
               ['John', 'Wiercinski', 'john.wiercinski@scranton.edu', 'HADM'],
               ['Matt', 'Montoro', 'matthew.montoro@scranton.edu', 'Counseling'],
               ['Sean', 'Youngblood', 'sean.youngblood@scranton.edu', 'HADM'],
               ['Jose', 'Sanchez', 'jose.sanchez@scranton.edu', 'Accounting'],
               ['Paul', 'Datti', 'paul.datti@scranton.edu', 'Counseling'],
               ['Laura', 'Stack', 'laura.stack@scranton.edu', 'HADM'],
               ['Gloria', 'Wenze', 'gloria.wenze@scranton.edu', 'Education'],
               ['Christian ', 'Krokus', 'christian.krokus@scranton.edu', 'Theology'],
               ['Kimberly', 'Subasic', 'kimberly.subasic@scranton.edu', 'Nursing'],
               ['John', 'Sailors', 'john.sailors@scranton.edu', 'Management'],
               ['Andrew', 'Milewski', 'andrew.milewski@scranton.edu', 'Education'],
               ['Kristen', 'Thomas', 'kristen.thomas@scranton.edu', 'CTLE'],
               ['Steven', 'Szdlowski', 'steven.szdlowski@scranton.edo', 'HADM'],
               ['Diane', 'Collens', 'diane.collens@scranton.edu', 'English'],
               ['Vanessa', 'Silla', 'vanessa.silla@scranton.edu', 'Education'],
               ['Rose', 'Termini', 'rosemary.termini@scranton.edu', 'CTLE'],
               ['Amanda', 'Ellard', 'amanda.ellard@scranton.edu', 'Counseling'],
               ['Jose', 'Sanchez', 'jose.sanchez@scranton.edu', 'Accounting'],
               ['Paul', 'Datti', 'paul.datti@scranton.edu', 'Counseling'],
               ['Laura', 'Stack', 'laura.stack@scranton.edu', 'HADM'],
               ['Gloria', 'Wenze', 'gloria.wenze@scranton.edu', 'Education'],
               ['Christian ', 'Krokus', 'christian.krokus@scranton.edu', 'Theology'],
               ['Kimberly', 'Subasic', 'kimberly.subasic@scranton.edu', 'Nursing'],
               ['John', 'Sailors', 'john.sailors@scranton.edu', 'Management'],
               ['Andrew', 'Milewski', 'andrew.milewski@scranton.edu', 'Education'],
               ['Kristen', 'Thomas', 'kristen.thomas@scranton.edu', 'CTLE'],
               ['Steven', 'Szdlowski', 'steven.szdlowski@scranton.edo', 'HADM'],
               ['Diane', 'Collens', 'diane.collens@scranton.edu', 'English'],
               ['Vanessa', 'Silla', 'vanessa.silla@scranton.edu', 'Education'],
               ['Rose', 'Termini', 'rosemary.termini@scranton.edu', 'CTLE'],
               ['Amanda', 'Ellard', 'amanda.ellard@scranton.edu', 'Counseling']]
    for obj in clients:
        add_client(c, obj[0], obj[1], obj[2], departments.index(obj[3]))

    types = ['CMS', 'Website', 'Visual Argument', 'Digitizing', 'Recording', 'Software', 'Research', 'Scanning',
             'CD/DVD', 'Miscellaneous', 'Professional Development', 'MS Powerpoint', 'MS Excel', 'MS Word', 'MS Access',
             'Windows Movie Maker', 'iMovie', 'Image Editing', 'PDF', 'File Conversion', 'Video', 'Desire  Learn',
             'Documentation', 'Cross Training']
    for obj in types:
        add_type(c, obj)
        # Print out what we have added to the user.
        # for c in Category.objects.all():
        #    for p in Page.objects.filter(category=c):


#        print "- {0} - {1}".format(str(c), str(p))
    conn.commit()
    conn.close()


def add_department(conn, name):
    params = (name, )
    conn.execute('INSERT INTO Department VALUES (NULL, ?)', params)


def add_client(conn, first_name, last_name, email, department):
    params = (first_name, last_name, email, department)
    conn.execute('INSERT INTO Client VALUES (NULL, ?, ?, ?, ?)', params)


def add_type(conn, name):
    params = (name, )
    conn.execute('INSERT INTO Type VALUES (NULL, ?)', params)

'''
def add_project(title, description, type, walk_in, client, users):
    p = Department.objects.get_or_create(title=title, description=description, type=type, walk_in=walk_in, 
                                         client=client, users=users)[0]
    p.save()
    return p
'''

# Start execution here!
if __name__ == '__main__':
    print("Populating database...")
    populate()
