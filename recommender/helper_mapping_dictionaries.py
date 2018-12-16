map_majors = {
	"Computer Sci.": ["computer science", "cloud computing"],
	"Information Sci./Tech.": ["information science", "information technology", "information systems"],
	"Computer Sci.-HCI":["hci", "hci/computer science", "human-computer interaction"], 
	"EE/CE": ["electrical engineering","electronic engineering", "computer engineering", "systems engineering", "electrical/mechanical/computer engineering", "software/electrical"],
	"Software Eng.": ["softwrae engineering", "software/electrical"],
	"Indus./Material/Mech. Eng.": ["industrial engineering", "materials engineering", "electrical/mechanical/computer engineering"],
	"Physics": ["physics"], 
	"Chemistry": ["chemistry"],
	"Biology": ["computational biology"],
	"Other Sciences": ["nutrition"],
	"Math/Statistics": ["applied mathematics", "mathematics", "statistics", "tatistics"],
	"Social Science": ["political science", "social sciences", "social science", "anthropology"],
	"Management/Communication": ["management information", "hotel management", "visual communications", "management information systems", "supply chain management"],
	"Psychology/Cognitive Science": ["psychology", "experimental psychology", "cognitive science"],
	"Operation Research":["operation research", "operations research"],
	"Business/Finance/Marketing": ["business administration", "finance",  "marketing", "business", "marketing field", "quantitative/business-oriented field", "supply chain", "business/commerce discipline", "quantitative/business"],
	"Economics": ["economics","econometrics","macroeconomics"],
	"Accounting": ["Accounting"],
	"Law": ["intellectual property"],
	"General - Analytics": ["analytical field", "analytics- related"],
	"General - Technical": ["technical field", "technical subject", "technical degree"],
	"General - Engineering": ["engineering field", "engineering discipline", "engineering"],#special case handeld in main code
	"General - Quantitative": ["quantitative field", "quantitative discipline", "quantitative analysis", "quantitative nature", "use quantative analysis", "quantitive field", "quantitative/business-oriented field", "quantitative/business"], #need to handle "quantitive" typo
	#"General - Low restriction": ["related field"],
	"General - Design": ["design", "graphic design", "industrial design"],
	"General - Linguistics": ["writing field", "linguistics"]
}

career_level_maps = {
						"Intern": ["Intern", "Apprenticeship"],
						"Associate/Assistant": ["Associate", "Assistant"],
						"Researcher/Scientist": ["Researcher", "Scientist"],
						"Engineer/Architect": ["Engineer", "Developer", "Architect"],
						"Analyst": ["Analyst"],
						"Trainer/Teacher": ["Teacher", "Trainer"],
						"HR": ["Recruiter", "Administrator"],
						"Consultant/Specialist/Representative": ["Consultant", "Specialist", "Representative"],
						"Manager/Advisor/Lead": ["Manager", "Advisor","Lead"],
						"Principal/Director/Head": ["Principal", "Director", "Head", "Chief of Staff"],
						"Executive/Partner": ["Executive", "Partner"],
						"Special positions - Legal": ["Counsel", "Copywriter", "Auditor"],
						"Special positions - Business/Finance": ["Controller", "Trader", "Negotiator", "Accountant"],
						"Special positions - Language": ["Linguist", "applied linguistics", "Editor", "Writer"],
						"Special positions - Design": ["Producer", "Designer"],
						"Special positions - Strategy": ["Strategist", "Investigator", "Advocate"]

					}

experience_areas_map = {
"A/B testing": ["a/b testing"],	
"Account manager/management": ["account manager", "account management"],
"Applied research": ["applied research"],
"Advertising": ["advertising", "advertisement"],
"ASP": ["asp"],
"Agreement discussions": ["leading agreement discussions"],
"Agreement management": ["agreement management"],
"Anaplan": ["anaplan"],
"Algorithm": ["algorithm"],					
"Accounting principles": ["gaap", "accounting principles"],
"ASIC": ["asic"],
"Adobe":["adobe test"],
"Automation": ["automation"],
"Applied math": ["applied mathematics"],
"Analytics field": ["analytics field"],
"Architect": ["solutions architect"],
"Agile partner": ["agile partner"],
"Application development":["application development"],
"Apache Pig": ["pig"],
"Authentication protocols": ["authentication protocols"],
"Audit": ["audit"],
"Big data": ["big data"],
"Biology": ["computational biologist/bioinformatician"],
"Business/Strategy": ["strategic business", "corporate strategies", "business analytics"],
"Business Administration": ["business administration"],
"Business intelligence": ["business intelligence"],
"Business training": ["business training", "business learner"],
"Business technology market": ["business technology market"],
"Business development": ["business development"],
"Configuration management": ["configuration management"],
"Corporate talent": ["in-house corporate talent"],

"Cross-functional": ["cross-functional"],
"CAD": ["cad tools integration"],
"C": ["C"],
"C/C++": ["C/C++"],
"C#": ["C#"],
"Contextual field visits": ["contextual field visits"],
"Conduct interviews": ["conducting semi-structured interviews"],
"Currency pair":["currency pair"],
"Client/partnership skills": ["client needs", "parterner-facing role", "customer facing", "technical customers", "customer", "partner", "customers", "client-facing"],
"Channel sales": ["channel sales"],
"Channel manager": ["channel manager"],
"Cloud computing": ["cloud computing"],
"Cloud architecture": ["cloud architecture"],
"Cloud platform": ["cloud platform"],
"Cloud market": ["cloud market"],
"Cloud solutions managment": ["managing cloud solutions"],
"Children": ["children"],
"Cound technologies": ["cloud technologies"],
"Competitive dynamics": ["competitive dynamics"],
"Customer buying behavior": ["customer buying behavior"],
"Customer/user service delivery": ["customer/user service delivery"],
"Compaign": ["compaign"],
"Change management": ["change-management"],
"Computational biology": ["computational biology"],
"Consulting experience": ["management consulting", "compensation consulting", "consulting firm", "consulting experience"],
"C++": ["c++"],
"Commodity management": ["commodity management"],
"Clickstream analysis": ["clickstream analysis"],
"Commodity": ["commodity"],
"Control design": ["control design"],
"Computer Science": ["computer science"],
"Computing environment": ["computing environment"],
"CSS": ["css", "css3"],
"CGI": ["cgi"],
"Hadoop": ["hadoop"],
"Corporate setting": ["corporate setting"],
"Computational statistics": ["computational statistics"],
"Commerce": ["commerce"],
"Contracted guard force": ["contracted guard force"],
"Communications": ["communications"],

"Data manipulation": ["data manipulation"],
"Database/Large dataset": ["commercial database", "large dataset", "large data set", "database querying", "database query", "database design"],
"Data warehousing": ["data warehousing"],
"Data analytics": ["data analytics", "data analysis", "analytics roles", "data definitions", "analyzing data", "analytics environment", "analyzing large data"],
"Data ingestion": ["pulling data"],
"Data structure": ["data structure"],
"Data visualization": ["data visualization", "visualization tools", "visualization platform"],
"Digital media": ["digital media"],
"Direct client sales/management": ["direct client sales/management"],
"Digital/mobile advertising sales": ["digital/mobile advertising sales", "digital advertising"],
"Development platform": ["development platform"],
"Data processing": ["data processing", "processing software", "processing algorithms"],
"DNS": ["dns"],
"Debugging": ["debugging"],
"Design manufactures": ["design manufacturers"],

"Executive recruiting": ["executive recruiting", "executive search", "executive search firm"],
"Executive selling": ["executive selling"],
"Equity": ["equity"],
"Experiment": ["experiment", "experimentation"],
"Electrical engineering": ["electrical engineering"],
"Enterprise software sales": ["selling enterprise software"],
"Enterprise software architecture": ["architecting enterprise software"],
"Encryption": ["encryption"],

"Front-end": ["front end"],
"Finance modeling/analysis": ["finance modeling", "finance analysis","finance functional area", "financial"],
"Firewalls": ["firewalls"],
"Full-stack": ["full-stack"],
"Federal government client": ["federal government client", "air force client"],
"Go": ["go"],
"Graphics":["graphics"],
"Global system integrators": ["global system integrators", "mid-tier integrators"],
"Hardware": ["hardware"],
"Healthcare": ["healthcare"],
"HEVC": ["hevc"],
"HTTP": ["http"],
"HTML": ["html", "html5", "xml/xslt/xhtml/html"],
"HIVE": ["hive"],
"Hyperion": ["hyperion", "hfm"],
"HR-related field": ["hr related field"],
"HPC": ["hpc", "high performance comput"],
"Linux shell": ["linux shell"],
"Linux-based platforms": ["linux-based platforms"],
"Java": ["java", "cgi/java/asp servlets"],
"J2EE": ["j2ee"],
"Java servlet": ["java servlet"],
"Juniper": ["juniper"],
"Kernal": ["kernal development"],
"Infant/toddler": ["infant/toddler"],
"Investment banking": ["investiment banking"],
"Industrial engineering": ["industrial engineering"],
"Information retrieval": ["information retrieval"],
"Information lifecycle management": ["information lifecycle management"],
"Industrial insights": ["industrial insights"],
"Informatica": ["informatica"],
"Ideation": ["ideation"],
"IoT": ["iot"],
"Life science": ["life science"],

"Lease administration": ["lease administration"],
"Load balancing": ["load balancing"],
"Mobile app devlopment": ["mobile application", "mobile app development"],
"Mobile marketing": ["mobile marketing"],
"Mobile websites": ["mobile websites"],
"Mobile management": ["mobile management", "emm"],
"Management role": ["management role"],

"Mobile OS": ["mobile os"],
"NLP processing": ["language processing"],
"Information technology": ["related it"],
"Issue identification": ["identifying issues"],
"Vendor software": ["vendor software"],
"Vendor management": ["vendor management"],
"Machine learning": ["machine learning"],
"Material design": ["material design"],
"Mapreduce":["mapreduce"],
"Marketing": ["marketing environment"],
"Management systems": ["management system"],
"Memory": ["memory"],
"Mobile platform": ["mobile platform"],
"Media performance report": ["media performance report"],
"Media analytics": ["media analytics"],
"Matlab": ["matlab"],
"Nodejs": ["nodejs"],
"Network": ["network"],
"Non-profit": ["nonprofit", "non-profit"],
"Virtual private networks": ["virtual private networks"],
"NPI": ["npi"],
"Operation research": ["operations research"],
"Oracle": ["oracle"],
"Operating system": ["operating system", "os"],
"Predictive analytics/modeling": ["forcasting", "predictive analytics"],
"Political science": ["political science"],
"Preschool": ["preschool"],

"PaaS": ["paas"],
"PHP": ["php"],
"Perl": ["perl"],
"Private equity firm": ["private equity firm"],
"Product management (PLM/PDM/Agile)": ["product management","PDM", "Agile", "PLM"],
"Product manager": ["Product manager"],
"Public training": ["public training provider"],
"Public relation": ["pr role"],
"Production service":["product questions"],
"Product research": ["research into product"],
"Program management":["program management"],
"Professional service": ["professional service"],
"Programming languages": ["programming language", "writing script", "programming/scripting languages"],
"Object-oriented Javascript": ["object-oriented javascript"],
"Outsourced operations": ["outsourced operations"],
"Javascript": ["javascript"],
"ODI": ["odi"],
"Optimization": ["optimization"],
"Parallel computing": ["parallel systems"],
"Production-grade": ["production-grade"],
"People management": ["people-related role", "people management"],
"Python": ["python"],
"PWA": ["pwa"],
"Process control": ["process control"],
"Quantitative field": ["quantitative field", "quantitative nature"],
"Quality management": ["quality management"],

"Qubit": ["qubit"],
"Qualitative research": ["qualitative research"],
"Ruby": ["ruby"],
"Relationships": ["relationship"],
"R&D":["r&d", "research and development"],
"Shell": ["shell"],
"Impala": ["impala"],
"Technical sales": ["Sales engineer", "technical sales", "technical pre-sales", "sales role"],
"Technical support": ["technical support"],
"SAP production planning": ["sap planning"],
"SAP portofolio": ["sap portfolio"],
"Scripting langugage": ["scripting language"],

"Security/Risk analysis/management": ["abuse signal", "threat analysis", "fraud risk", "risk management", "fraud", "managing security operations"],
"Advanced security matters": ["advanced security matters"],
"Shared codebase": ["shared codebase"],
"Social science": ["social science"],
"Statistical analysis/modeling": ["statistical analyses", "statistical analysis", "statistical packages", "statistical software","statistician","data scientist", "statistics"],
"Software development": ["software development", "writing software"],
"Software sales": ["software sales"],
"file systems": ["shared file systems"],
"Software design": ["software design"],
"Sales enablement": ["sales enablement"],
"Software system": ["software system"],
"Supply chain": ["supply chain"],
"Supply chain management": ["supply chain managment"],
"Survey design": ["survey design"],
"Site oepration": ["site operation"],
"Science backgroud": ["sciences related", "science domain"],
"Solutions architect": ["solutions architect"],
"Scalable partner ecosystems": ["scalable partner ecosystems"],
"Partner management/B2B support": ["partner management/b2b support"],
"Satisfaction metrics": ["satisfaction metrics"],
"Measuring success": ["measuring success"],
"Partner development": ["partner development"],
"B2B marketing": ["b2b marketing"],
"Marketing research": ["market research"],


"System engineering/implementation": ["system implementation", "system engineering","systems engineering"],
"System administration": ["system administration", "systems administration"],
"SQL": ["sql coding", "sql-based quer", "mysql" ],

"Third-party": ["3rd party", "3rd-party", "third part", "third-party"],
"Technology martket": ["technology market"],
"Technology industry": ["technology industry", "technology company", "technology firm", "high tech", "high-tech"],
"SDN/SDK": ["sdn", "sdk"],
"Spark": ["spark"],
"SAS": ["sas"],
"SaaS": ["saas"],
"Stata": ["stata"],
"S-plus": ["s-plus"],
"Stakeholder": ["stakeholders"],
"R": [" r "],

"Infrastructure": ["infrastructure"],
"IaaS (infrastructure-as-a-service)": ["iaas", "infrastructure-as-a-service"],
"Integrated circuit": ["integrated circuit"],

"Recruiting/Staffing": ["Recruiting", "Recruitment", "recruiting experience", "staffing role"],

"Tax": ["employment tax", "corporate tax", "tax department"],
"Tehcnology industry sales": ["technology industry sales"],
"Sales": ["sales"],
"Technology sector": ["technology sector"],
#"Training provider": ["training provider"],
"Technical field": ["technical field"],
"Internet protocols": ["tcp/ip", "routing protocols", "ospf", "mpls"],
"International law": ["international law"],
"Law": ["Law"],
"Legal contract": ["legal contract"],
"Legal assistant": ["legal assistant"],
"Legal agreement": ["legal assistant"],


"Windows": ["windows 2008 r2", "2012 r2", "windows deployments"],
"Web analytics": ["web analytics"],
"Web services": ["web services"],
"Web development": ["web development", "web technologies", "web application", "web standard", "develoing websites"],

"Unix/Linux": ["unix systems", "unix/linux", "linux"],

"UPF/CPF":["upf/cpf"],
"User focused": ["user focused"],
"User research": ["user research", "ux research"],
"Usability studies": ["usability studies"],
"UX development": ["ux development", "ux"],
"UX design": ["ux design"],
"US air force/navy/army": ["us air force", "us navy", "us army"],
"UserZoom": ["user zoom"],
"Virtualization": ["virtualization"],
"Video technologies": ["video", "video streaming", "video archiectures"],
"Vendor managment": ["vendor management"],
"VNA/ENA": ["vna/ena"],
"Verilog": ["verilog"],
"Verification": ["verification"],
"Validation": ["validation"],
"Venture capital": ["venture capital"],
"xml": ["xml/xslt/xhtml/html", "xml"]
						}

#color_array = ['r','y','b','g','b','c','m']
map_major_colors = {
	"Computer Sci.": "g",
	"Information Sci./Tech.": "y",
	"Computer Sci.-HCI":"g", 
	"EE/CE": "m",
	"Software Eng.": "g",
	"Indus./Material/Mech. Eng.": "r",
	"Physics": "r", 
	"Chemistry": "r",
	"Biology": "r",
	"Other Sciences": "r",
	"Math/Statistics": "b",
	"Social Science": "m",
	"Management/Communication": "m",
	"Psychology/Cognitive Science": "m",
	"Operation Research":"y",
	"Business/Finance/Marketing": "c",
	"Economics": "c",
	"Accounting": "c",
	"Law": "r",
	"General - Analytics": "k",
	"General - Technical": "k",
	"General - Engineering": "k",#special case handeld in main code
	"General - Quantitative": "k", #need to handle "quantitive" typo
	#"General - Low restriction": ["related field"],
	"General - Design": "k",
	"General - Linguistics": "k"
}

