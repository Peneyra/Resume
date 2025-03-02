import yaml
from pathlib import Path

file_path = "./resume.yaml"

# Initialize
if not Path(file_path).exists():
    init = {}
    with open(file_path,"w") as file: yaml.safe_dump(init,file)

with open("resume.yaml","r") as file: r = yaml.safe_load(file)

r['professional experience'] = [
    {
        'Google Public Sector - SLED & Federal': [
            {
                'Cloud Program Manager (SkillBridge Fellow)': {
                    'location': "Remote",
                    'timestart': "January 2025",
                    'timeend': "Present",
                    'bullets': [
                        "PM for the development of a Gemini-based Adjudication Assistant for New Hampshire Employment Security, leveraging Gen-AI for fact-finding and compliance assurance. This initiative aimed to significantly alleviate workload constraints caused by a critical shortage of experienced adjudicators statewide.",
                        "PM for the development of a Google Cloud infrastructure setup and modernization for Colorado’s State Verification and Exchange System (SVES). The updated SVES application will leverage cloud architecture, security, and authentication systems to provide a modernized workflow and user interface.",
                        "PM for the development and integration of a scalable, cloud based, and API-centered platform for the US Air Force Rapid Sustainment Office’s (RSO) Lighthouse Integration Technology Engine (LITE) for distributed functionality across aircraft maintenance management software. This project will provide a flexible, secure, and scalable solution to daily maintenance activities and flightline operations."
                    ]
                }
            } 
        ]
    }, {
        'Submarine Officer, Lieutenant Commander, United States Navy (DoD)': [
            {
                'Group Operations Director – Command Task Group 114.3': {
                    'location': "Bangor, WA",
                    'timestart': "March 2024",
                    'timeend': "Present",
                    'bullets': [
                        "Developed Python software which utilizes discrete Fourier transforms and numerical change of basis to accomplish 1 to 4500 compression of weather images, enabling transmission of critical operational planning information to submarines with limited bandwidth, enhancing the safety and efficacy of worldwide submarine operations. This saved the Navy $150,000 in software development costs.",
                        "Authored precise execution orders to enable seamless integration across diverse military platforms during key operations, resulting in the first successful 30-day replenishment of an at-sea ballistic missile submarine, extending the operational availability of a single unit by 40% to enhance strategic readiness of the forces. The underway replenishment provided a $250,000 cost savings compared to alternative methods of extending submarine operations.",
                        "Authored precise execution orders to enable seamless integration across diverse military platforms during key operations, resulting in the inaugural integrated operations between A-10 airframes and an SSBN, which created a new method of providing underway force protection to a ballistic missile submarine, enhancing the security and safety of the force.",
                        "Directed, led, and managed the day-to-day operations of seven Ballistic Missile Submarines and 2,500 sailors in the Pacific, managing long term schedules and the strategic outlook for the force, using predictive metrics to optimize asset availability and generate executive level reports, ensuring the effective utilization of ~$14B in assets and operating costs, while collaborating with global stakeholders to optimize the allocation of operational time for these seven Ballistic Missile Submarines, maximizing the achievement of strategic priorities. Successfully ensured mission readiness and operational effectiveness through cross-organizational planning, resource allocation, and performance management. Analyzed historical submarine utilization data to compare operational schedules against the Ohio-class model, identifying imbalances in unit deployment cycles. Leveraged these insights to project and refine future schedules, resulting in a 10% increase in overall operational availability."
                    ]
                }
            }, {
                'Unit Operations Director – USS Henry M Jackson (SSBN 730)': {
                    'location': "Bangor, WA",
                    'timestart': "October 2020",
                    'timeend': "March 2024",
                    'bullets': [
                        "Developed a Visual Basic application to automate a manual process for processing and visualization of maritime traffic data, reducing processing time by 90%. This application ingested Integrated Broadcast System CSV files, extracted key information, and generated KML files for display on Google Earth, enabling long-term tracking of merchant vessels and enhancing submarine safety during submerged operations.",
                        "Developed a reproducible pseudo-random image using RSA algorithms to simulate background noise. This image was used in a sonar training simulation, demonstrating the practical application of cryptographic principles and teaching early submariners the fundamentals of contact management.",
                        "Spearheaded the planning and execution of four submarine patrols, writing the daily operational schedule to balance competing priorities across four departments and multiple stakeholders. Required to schedule, track, and report on multiple long-term projects for research and development. Self driven work ethic and excellent interpersonal and communication skills led to being recognized as the top-ranking department head among 56 peers.",
                        "Used engineering drawings to develop tailored troubleshooting and repair plans, ensuring rapid resolution of equipment failures for systems worth $100M, minimizing downtime and optimizing operational readiness.",
                        "Developed and maintained the ship’s website using html, css, js, and php, consolidating key documents, streamlining access to resources, and helping with the dissemination of information.",
                        "Oversaw the maintenance and operations of communication, electronic warfare, and navigation equipment aboard the submarine, leading a team of 7 direct reports and 30 indirect reports.",
                        "Led a watch team responsible for the effective and safe operation of the ballistic missile submarine in a fast-paced, high-stakes environment, serving as the lead decision maker during simulated wartime scenarios."
                    ]
                }
            }, {
                'Scheduling Director – Command Seventh Fleet': {
                    'location': "Yokosuka, Japan",
                    'timestart': "May 2017",
                    'timeend': "October 2020",
                    'bullets': [
                        "Directed mission, maintenance, and training schedules for 70 ships, 150 aircraft, and 27,000 sailors. Also integrated Carrier Strike Group operations across an Aircraft Carrier, 2 Cruisers, 4 Destroyers, 3 Airwings and 7,500 sailors. These efforts contributed to operational readiness in the INDOPACIFIC region, the Navy's largest forward-deployed fleet, and supported power projection and joint exercises with Pacific partners during four 3-month patrols.",
                        "Developed a database of operational metrics to automate readiness reporting, which was previously a manual data-gathering process. This streamlined asset allocation decisions, reducing report generation time by 90% and report generation costs by $50K annually.",
                        "Developed a suite of Visual Basic programs coupled with Excel to predict operational metrics and identify capability gaps in ship schedules. This enabled executive-level decision-makers to make data-driven decisions to allocate resources.",
                        "Collaborated with multiple stakeholders to prioritize asset allocation across the largest naval fleet in the world and ensured effective strategic messaging to regional partners."
                    ]
                }
            }, {
                'Submarine Warfare Officer – USS Pasadena (SSN 752)': {
                    'location': "San Diego, CA",
                    'timestart': "April 2013",
                    'timeend': "May 2017",
                    'bullets': [
                        "Directed a team of 40 personnel across nuclear reactor controls and tactical weapons systems, enforcing rigorous maintenance, operations, and training standards while meticulously managing training, certification, audit, and surveillance programs.",
                        "Coordinated 26 watch standers in operating and maintaining a nuclear submarine in a high-stress environment, directly contributing to missions vital to national security.",
                        "Spearheaded the first submarine-launched drone program to be used in theater, leading training, certification, and operations for four drone pilots, and assisting in the development of operational doctrine, which resulted in the first-ever drone operation from a submarine while on mission.",
                        "Demonstrated expertise in communicating complex technical concepts, evidenced by earning qualification as an Engineering Officer in the Navy Nuclear Propulsion program."
                    ]
                }
            }
        ] 
    }
]


print(r)
with open("resume.yaml","w") as file: yaml.safe_dump(r,file)