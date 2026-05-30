Identify

Analyse

Mitigate

Task 13  Performance, Operation and Reliability of Photovoltaic Systems

S
P
V
P

Quantification of
Technical Risks in
PV Power Systems
2021

Report IEA-PVPS T13-23:2021

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

What is IEA PVPS TCP?

The International Energy Agency (IEA), founded in 1974, is an autonomous body within the framework of the Organization for Ec onomic

Cooperation and Development (OECD). The Technology Collaboration Programme (TCP) was created with a belief that the future of energy

security and sustainability starts with global collaboration. The programme is made up of 6.000 experts across government, ac ademia, and

industry dedicated to advancing common research and the application of specific energy technologies.

The IEA Photovoltaic Power Systems Programme (IEA PVPS) is one of the TCP’s within the IEA and was established in 1993. The mission

of the programme is to “enhance the international collaborative efforts which facilitate the role of photovoltaic solar energy as a cornerstone

in the transition to sustainable energy systems.” In order to achieve this, the Programme’s participants have undertaken a va riety of joint

research projects in PV power systems applications. The overall programme is headed by an Executive Committee, comprised of one dele-

gate from each country or organisation member, which designates distinct ‘Tasks,’ that may be research projects or activity areas.

The IEA PVPS participating countries are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany, Israel,

Italy, Japan, Korea, Malaysia, Mexico, Morocco, the Netherlands, Norway, Portugal, South Africa, Spain, Sweden, Switzerland,  Thailand,

Turkey, and the United States of America. The European Commission, Solar Power Europe, the Smart Electric Power Alliance (SEPA), the

Solar Energy Industries Association and the Cop- per Alliance are also members.

Visit us at: www.iea-pvps.org

What is IEA PVPS Task 13?

Within the framework of IEA PVPS, Task 13 aims to provide support to market actors working to improve the operation, the reliability and the

quality of PV components and systems. Operational data from PV systems in different climate zones compiled within the project will help

provide the basis for estimates of the current situation regarding PV reliability and performance.

The general setting of Task 13 provides a common platform to summarize and report on technical aspects affecting the quality, performance,

reliability and lifetime of PV systems in a wide variety of environments and applications. By working together across national boundaries we

can  all  take  advantage  of  research  and  experience  from  each  member  country  and  combine  and  integrate  this  knowledge  into  valu able

summaries of best practices and methods for ensuring PV systems perform at their optimum and continue to provide competitive return on

investment.

Task 13 has so far managed to create the right framework for the calculations of various parameters that can give an indication of the quality

of PV components and systems. The framework is now there and can be used by the industry who has expressed appreciation towards the

results included in the high-quality reports.

The IEA PVPS countries participating in Task 13 are Australia, Austria, Belgium, Canada, Chile, China, Denmark, Finland, France, Germany,

Israel, Italy, Japan, the Netherlands, Norway, Spain, Sweden, Switzerland, Thailand, and the United States of America.

DISCLAIMER

The IEA PVPS TCP is organised under the auspices of the International Energy Agency (IEA) but is functionally and legally autonomous. Views, findings and publica-

tions of the IEA PVPS TCP do not necessarily represent the views or policies of the IEA Secretariat or its individual member countries.

COVER PICTURE

In the back, inspection of a PV power plant after a severe storm. Photo curtesy of TÜV Rheinland.

In the front, practices of risk quantification divided into an adapted rating system by SUPSI/Sinclair, analysis methods and mitigation by TÜV Rheinland.

ISBN 978-3-907281-11-6: Quantification of Technical Risks in PV Power Systems

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

INTERNATIONAL ENERGY AGENCY

PHOTOVOLTAIC POWER SYSTEMS PROGRAMME

IEA PVPS Task 13
Performance, Operation and
Reliability of Photovoltaic Systems

Quantification of Technical Risks in
PV Power Systems

Report IEA-PVPS T13-23:2021
October 2021

ISBN 978-3-907281-11-6

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

AUTHORS

Main Authors

Magnus Herz, TÜV Rheinland, Cologne, Germany

Gabi Friesen, SUPSI-PVLab, Mendrisio, Switzerland

Ulrike Jahn, VDE Renewables, Alzenau, Germany

Marc Köntges, ISFH, Emmerthal, Germany

Sascha Lindig, EURAC Research, Bolzano, Italy

David Moser, EURAC Research, Bolzano, Italy

Contributing Authors

Stefan Bordihn, ISFH, Emmerthal, Germany

Gabriele Eder, OFI, Vienna, Austria

Uwe Hupach, TÜV Rheinland, Cologne, Germany

Guillermo Oviedo Hernández, BayWa r.e., Rome, Italy

Bert Herteleer, KU Leuven, Gent, Belgium

Werner Herrmann, TÜV Rheinland, Cologne, Germany

Jay Lin, PV Guider Consultancy, Taipei, Taiwan

Christian Schill, Fraunhofer ISE, Freiburg, Germany

Editors

Magnus Herz, TÜV Rheinland, Cologne, Germany

Ulrike Jahn, VDE Renewables, Alzenau, Germany

4

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

TABLE OF CONTENTS

Acknowledgements .................................................................................................. 6

List of Abbreviations ................................................................................................. 7

Executive Summary ................................................................................................. 9

INTRODUCTION ............................................................................................. 11

  COMMON  PRACTICE  FOR  QUANTIFYING  THE  IMPACT  OF  TECHNICAL
RISKS ............................................................................................................. 12

2.1  Key Definitions ....................................................................................... 12

2.2  Semi-Quantitative Methods (FMEA, MCDA) ........................................... 13

2.3  Quantitative Methods (CPN, RAM) ......................................................... 14

2.4  Risk Mitigation Measures ....................................................................... 19

2.5  Best Practice, Limitations and Challenges .............................................. 20

  RISK DATABASE ............................................................................................ 21

3.1  PV Failure Fact Sheets (PVFS) .............................................................. 21

3.2  PV Failure Degradation Sheets (PVDS) ................................................. 27

3.3  PV Cost Data.......................................................................................... 35

  CASE STUDIES .............................................................................................. 36

4.1  Risk Analysis .......................................................................................... 36

4.2  Cost-Benefit Analysis ............................................................................. 38

  CONCLUSIONS .............................................................................................. 42

References ............................................................................................................. 43

ANNEX 1 ................................................................................................................ 48

5

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

ACKNOWLEDGEMENTS

This  paper  received  valuable  contributions  from  several  IEA-PVPS  Task  13  members  and
other international experts. Many thanks for reviewing and editing the report to:

Karl Berger, AIT, Austria

Roger H. French, Case Western Reserve University, USA

Matthias Littwin, ISFH, Germany

Jan Vedde, European Energy, Denmark

This  report  is  supported  by  the  German  Federal  Ministry  for  Economic  Affairs  and  Energy
(BMWi) under contract no. 0324304A, 0324304B and 0324304C.

This  report  is  supported  by  the  Swiss  Federal  Office  of  Energy  (SFOE)  under  the  contract
SI/501788-01 and SH/8100038-02-02-02.

6

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

LIST OF ABBREVIATIONS

AC

AHP

BYT

Alternating Current

Analytic Hierarchy Process

Bypass Diode testing

CAPEX

Capital Expenditures

CPL

CPN

D

DC

dIV

EL

Component Power Loss

Cost Priority Number

Detectability

Direct Current

Dark I-V Measurement

Electroluminescence

EPC

Engineering, Procurement, Construction

FMEA

Failure Modes and Effects Analysis

FTA

IEA

INS

IRT

I-V

KPI

LCOE

LeTID

LID

Fault Tree Analysis

International Energy Agency

Insulation Testing

Infrared Thermography

Current-Voltage

Key Performance Indicator

Levelised Cost of Electricity

Light and elevated temperature induced degradation

Light induced degradation

MCDA

Multi Criteria Decision Analysis

MDT

MM

MON

MTTF

NPV

O

O&M

OPEX

PDF

PID

Mean Down Time

Mitigation Measure

Data Monitoring

Mean Time To Failure

Net Present Value

Occurrence

Operation and Maintenance

Operational Expenditures

Probability Density Function

Potential Induced Degradation

PMBOK

Project Management Body of Knowledge

PLR

PR

PV

Performance Loss Rate

Performance Ratio

Photovoltaic

7

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

PVDS

PVFS

PVPS

RAM

RBD

RDB

RPN

S

SRD

STL

STM

UV

VI

PV Failure Degradation Sheet

PV Failure Fact Sheet

PV Power Systems

Reliability, Availability, and Maintainability

Reliability Block Diagram

Risk Database

Risk Priority Number

Severity

Statistical Risk Data

Seasonal-Trend Decomposition using LOESS

Signal Transmission Method

Ultra Violet

Visual Inspection

VOC

Voc Measurement

8

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

EXECUTIVE SUMMARY

Photovoltaic (PV) risk analysis serves to identify and reduce the risks associated with invest-
ments in PV projects. The key challenge in reacting to failures or avoiding them at a reasonable
cost is the ability to quantify and manage the various risks. There are several interpretations
of the concept of risk, but in general risk can be defined as the probability of failure multiplied
by the consequences of its failure.

Best practice guidelines to improve the operation of PV power systems are often only applied
as  long  as  the  recommended  actions  have  advantages  for  the  executors,  the  Engineering,
Procurement, Construction (EPC) and Operation and Maintenance (O&M) companies and for
the investors whose main interests focus on low risks and maximum profit from an economic
point of view. This leads to the key question: How can you demonstrate the effectiveness of
measures and justify their application? Because the technical best solution is not always the
economic best solution. And before you are able to evaluate the cost-benefit ratio, the following
question arises: How to quantify the basic impact of technical risks on performance and relia-
bility?

In a first approach we reviewed scientific literature and technical reports to compare and as-
sess the common practices for quantifying the impact of technical risks. Limitations and chal-
lenges were compiled and selection criteria defined for the four methods:

a)  Failure Modes and Effects Analysis (FMEA)
b)  Multi Criteria Decision Analysis (MCDA)
c)  Reliability, Availability, and Maintainability (RAM) analysis
d)  Cost Priority Number (CPN) method

The advantages and disadvantages of these methods are demonstrated considering the fac-
tors  maturity  level  and  data  availability,  and  as  well  an  overview  of  common  risk  mitigation
measures is given.

The second part deals with 30 PV Failure Fact Sheets (PVFS) annexed to this report which
summarise some of the most important aspects to know about single failures. The target au-
dience for these PVFSs are PV planners, installers, investors, independent experts and insur-
ance companies or anyone interested in a brief description of failures with examples, an esti-
mation  of  risks  and  suggestions  of  how  to  intervene  or  prevent  these  failures.  Besides  the
PVFS collection we used a PV Failure Degradation Sheet (PVDS) as introduced in [1]. These
requires much more detailed measured input data but are able to provide statistics on degra-
dation rates and power loss of PV systems based on failure types. Compared to the survey
structure in [1] we added two new failure categories for PV modules: Light and elevated tem-
perature induced degradation (LeTID) and potential induced delamination.

These statistics serve as a basis for risk models, such as the CPN method [2] [3], which are
used to assess the associated risk and the economic impact over the project-lifetime of a PV
plant. In addition to the knowledge of the individual risks, the economic impact of these risks
are  driving  factors  for  further  analysis  and  decisions.  In  a  final  step  the  costs  of  mitigation
measures are included in a cost-benefit analysis in order to derive the best strategy from a
technical and financial perspective.

The revised CPN approach is presented through an exemplary calculation of individual CPN
values. The CPN approach was applied to 191 maintenance tickets of a PV plant located in

9

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

central Italy which is in operation since 2013. The maintenance tickets were analysed manu-
ally, corresponding to all the planned and corrective activities carried out in 2018 for the exam-
ple plant. The improved CPN methodology has been applied manually to this case study, which
led to important improvements, especially in terms of the structure and standardisation of the
CPN table. We conclude that the development of an automated, and therefore time-efficient,
solution for extracting key parameters from maintenance tickets is of vital importance for the
implementation of this methodology at the portfolio level, and thus, to gain statistical insights
from a large number of PV plants.

In a second case study the CPN method was also applied to a 10 MWp PV plant. As one of
the main risks for the PV modules, potential induced degradation (PID) was selected. Taking
Capital Expenditures (CAPEX), Operational Expenditures (OPEX) and annual revenues into
account, the project’s financial profit after 20 years of operation was 48% below original ex-
pectations. Considering the additional costs of mitigation measures, the loss on the cumulated
financial income after 20 years of operation could be kept at only 5% - 6% below the originally
expected profit.

Cleaning routines for PV power systems in desert regions are a typical corrective measure to
reduce energy yield losses due to soiling. The impact of different cleaning procedures on the
soiling losses over one year are calculated and shown for a 10 MWp PV plant near Abu Dhabi.
In the case of periodic (monthly) cleaning, annual energy losses due to soiling are reduced
from 30% to 4% including the costs of 12 cleaning routines. The best economic results are
achieved with “triggered cleaning” at a soiling loss of 5%, even if 20 cleaning routines per year
are required. The calculations showed how it is possible to determine the best economic solu-
tion for a specific PV plant, loss scenario and mitigation approach.

With the provided overview of quantification methods, we draw the conclusion that more stand-
ardisation is required. Risk definitions are not fully structured and event databases (solar log-
books) are not harmonised. The development of a software tool for field technicians is recom-
mended that would allow the precise and error-free recording of standardised parameters for
the calculation of the O&M contractor’s Key Performance Indicators (KPI) necessary for effi-
cient implementation of the methodology [4]. In summary the O&M field practices must  cer-
tainly move away from the manual input of tickets in text format and adopt a more standardised
approach where human intervention is limited.

All things considered, we believe that the data-driven evaluation and modelling of techno-eco-
nomic performance indicators is a significant key to take decision support on Levelised Cost
of Electricity (LCOE) to the next level.

10

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

  INTRODUCTION

Technical risks are important criteria to be considered when investing in new and existing PV
installations. Quantitative knowledge of these risks is one of the key factors for the multiple
types of stakeholders, such as asset managers, banks or project developers, to define reliable
business decisions before and during the operation of their PV assets.

While multiple interpretations of the concept of risk exist, it is generally agreed that risk can be
defined  as  the  probability  of  failures  multiplied  by  the  consequences  of  these  failures.  The
common approach in evaluating technical risks is to apply a classical FMEA [5]. It is widely
used in the automotive, aerospace, and electronics industries to identify, rank, and mitigate
potential failures. Root cause and impact of a failure can be analysed. The disadvantage of
this approach is that the risk is evaluated in a qualitative way and cannot provide a framework
for the calculation of the economic impact. Thus, a cost-based FMEA was proposed in 1993
[6] and enhanced in 2003 [5]. Several applications of cost-based FMEA can be found in the
literature [7], often related to automotive or wind energy [8].

In 2017, a cost-based FMEA was presented within the Solar Bankability Project [9] as a first
attempt to implement a cost-based FMEA to the PV sector. The metric CPN was applied as
one KPI for the risk assessment of PV investments. In [4], the CPN method was further devel-
oped  with the  focus on  the  needs  of  large  O&M operators.  Other  publications  [10] [11]  dis-
cussed the topic from a reliability perspective. As by definition, if you enhance the reliability of
the system's components, the overall system risk is reduced.

The aim of this report is to increase the knowledge of methodologies to assess technical risks
and mitigation measures in terms of their economic impact and effectiveness during operation
& maintenance and to investigate the most important risks by collecting case studies and up-
dating the database with the acquired information. Based on results from previous work yield
assessments for new projects [12], monitored loss rates for existing power plants [13] [14] and
the relevant financial parameters [15] decisively determine the impact of technical risks on Net
Present Value and the Levelised Cost of Electricity.

In Chapter 2, common practices for quantifying the impact of technical risks were compared
and a list of recommended mitigation measures tailored to the identified risks and the status
of the PV plant is developed. After a first review of the scientific literature and technical reports,
the limitations and challenges are compiled, and selection criteria defined.

Chapter 3 deals with the systematical approach to identify the main technical risks and collect
these failure, loss and occurrence data from previous IEA PVPS Task 13 reports [16] [1]. These
statistics can then serve as the basis for risk models which are used to assess the associated
risk  and  the  economic  impact  over  the  project-lifetime  of  a  PV  plant.  In  addition  to  the
knowledge of the individual risks, the economic impact of these risks are the driving factors for
further analysis and decisions.

In Chapter 4, real case studies are introduced. The costs of mitigation measures are included
in  a  cost-benefit  analysis  in  order  to  derive  the  best  strategy  from  a technical  and financial
perspective.

11

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

  COMMON  PRACTICE  FOR  QUANTIFYING  THE  IMPACT

OF TECHNICAL RISKS

According to the Project Management Body of Knowledge (PMBOK) guide, a set of standard
terminology and guidelines for project management [17], “Risk quantification is a process to
evaluate  identified  risks  to  produce  data that  can  be  used  in  deciding  a  response  to  corre-
sponding risks”. This implies that the first step is to identify the technical risks and subsequently
determine the probability of occurrence and the impact on the energy yield. Previous works
within IEA PVPS Task 13 [16] [1], Moser et al. [2] and the PV failures fact sheet in Chapter 3.1
have identified and described the most common technical failures that could impact the per-
formance of a PV power plant. In addition to failures, there are also other technical risks during
operation caused by varying performance loss rates as analysed in [18] [14]. How to respond
to these risks with preventive or corrective actions is discussed by Jahn et al. in [3] and [19].
In the following, these evaluation processes are classified into semi-quantitative and quantita-
tive methods with a focus on photovoltaics. This chapter gives an insight into common methods
used, how technical risks in PV plants can be evaluated and minimised, and provides recom-
mendations for best practices.

2.1  Key Definitions

While there are specific parameters for each quantification method, this chapter presents the
recurring indicators typically used in contracts in the PV sector (s. Figure 1). Further definitions
can be found in the Task 13 report [12] or [20].

Technical risk: The probability of problems multiplied by the consequences of its failure.

Reliability: The probability that a component performs its intended function

Energy Yield: The electrical energy generated by a power plant.

Yield Loss: Not-generated energy caused by a problem.

Failure rate: It indicates how many objects fail on average in a period of time.

Detection time: How long a problem exists before it is noticed.

Response time: Time between when the problem is detected and the corrective action starts.

Resolution time (repair time): time to resolve the fault from the moment of reaching the plant.

Figure 1: Parameters to calculate the O&M contractor KPIs, extracted from the monitor-
ing and ticketing system [19].

12

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

2.2  Semi-Quantitative Methods (FMEA, MCDA)

These  semi-quantitative  methods  use  human  problem-solving  strategies,  based  on  expert
knowledge and expert opinion. The best ways to use such a knowledge-based method is to
conduct on- or offline workshops where experts can discuss and consequently assign values
to the risks identified. They can prioritise the identified risks using a pre-defined rating scale.
Risks will be scored based on their probability or likelihood of occurrence and their impact.

2.2.1  FMEA

One typical approach is a classic Failure Modes and Effects Analysis [21]. In the FMEA, each
identified risk is evaluated for its Severity (S), Occurrence (O) and Detectability (D).

𝑅𝑃𝑁 =  𝑆  ∙  𝑂  ∙  𝐷

(1)

With the resulting Risk Priority Number (RPN) the evaluated risk can be ranked and compared
with other risks. Figure 2 gives an example of FMEA rating of PV module failures. The disad-
vantage of this approach is that further usage, i.e. within a financial model, is limited [2].

Figure 2: Example of rating of PV module failures based on classic FMEA. The rating of
the technical risks was based on the statistics of failure reports from TÜV Rheinland.
RPN is the product of S, O and D where each factor is an integer between 0 and 10 [2].

2.2.2  MCDA

Another class of methods is the Multi Criteria Decision Analysis [22]. MCDA methods use re-
lationships such as priority, outranking and distance between the criteria. It is similar to FMEA;
however, it solves the biased subjective ranking within FMEA, as each single variable is addi-
tionally weighted.

One MCDA known for robustness is the Analytic Hierarchy Process (AHP) method developed
by  Saaty  [23].  It  is  based  on  three  principles:  building  hierarchies,  priority  and  logical  con-
sistency. Priorities are absolute numbers between 0 and 1 and always add up to 1. Figure 3

13

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

shows the calculated priorities to determine the optimal location for a large PV plant in southern
Iran [24].

Figure 3: Example of AHP priorities to determine the optimal PV plant location in south-
ern Iran. The sum of all priorities is equal to 1. Adapted from [24].

2.3  Quantitative Methods (CPN, RAM)

Quantitative Methods involve assessing the probability and impact of risks using numerically
based techniques, such as simulation and fault tree analysis. The results provide information
about the effects of the identified risks and represent a given reality in the form of a numerical
value that can be utilized in economic and financial models for quantitative decision making.

2.3.1  Cost Priority Number (CPN)

In this sub-section, the CPN methodology, a method originally developed for PV systems in
the H2020 project Solar Bankability [9], is discussed.

CPN was developed in the early 2000’s to address the fact that FMEA was unable to be used
for quantitative financial assessments. Therefore Cost-based FMEA was proposed. The FMEA
community had already developed the Risk Priority Number (RPN). When full lifecycle analysis
[25] of large projects such as the “Next Linear Collider” were being designed and priced, full
lifecycle costs, considering not just construction, but O&M, repairs and loss of production time,
and FMEA needed to be taken into account [26]. In 2003 [27] this was formalized as Cost-
based FMEA [5], as an extension of the RPN used previously [7]. And in the ensuing years the
utility of connecting FMEA to lifecycle costs and financial decision making was introduced in
many engineering fields [8] [28], with Kahrobaee et al. [29] introducing CPN in a lifecycle and
FMEA analysis of wind turbine systems.

For PV systems CPN enables accurate economic quantification of PV degradation modes and
other performance impairing effects of operating PV plants. It therefore has enabled risk as-

14

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

sessments  of  investments  in  PV  power  plant  projects  [2].  The  CPN  methodology  used  as-
sessed the economic impact of PV projects based on factors such as performance loss and
downtime. Thereby, a cost-based Failure Mode and Effect Analysis methodology for the PV
sector has been developed in form of the CPN. In its initial form, it was developed using theo-
retical scenarios to calculate extreme values for the CPN metric, expressed in €/kWp/year (see
Figure 4). Thereby, all phases of a PV power plant’s life cycle (from product testing to decom-
missioning) have been included. The methodology helps to identify and classify technical risks
and their economic impact by assigning a cost metric that, based on collected statistics, sup-
ports preventive and corrective measures, which would then lower the impact of failures on the
availability and performance of a PV plant. Thereby, it was possible to create a database which
gives indicators of failure appearance likeliness and severity. Such results could then be used
to improve O&M activities.

Figure 4: CPN, repair costs and performance losses for top 10 risks for PV modules [30].

An important improvement of the methodology was the integration of monitoring data to calcu-
late realistic CPN values for individual PV system performance impairments [4]. Thereby, the
focus is on the operation and maintenance (O&M) phase which is by far the longest one in the
life cycle of a PV plant (20-25 years). Real monitoring data were used, and information was
extracted from maintenance tickets to improve the accuracy of the methodology by stepping
away from theoretical assumptions. In order to calculate the cost due to the performance im-
pairment arising from a system failure, the downtime is divided into time intervals defined in
Chapter 2.1 [20]. According to the CPN methodology, costs related to the appearance of spe-
cific failures can be calculated as:

𝑪𝑷𝑵 [€/𝑘𝑊𝑝/𝑦𝑒𝑎𝑟]   =   𝐶𝑑𝑜𝑤𝑛   +   𝐶𝑓𝑖𝑥

𝑃𝑅𝑓𝑎𝑖𝑙[%] = 𝑃𝑅𝑠𝑡𝑎𝑟𝑡,𝑚𝑜𝑛 − 𝑃𝐿𝑅 ∗ (𝑦𝑒𝑎𝑟𝑓𝑎𝑖𝑙 − 𝑦𝑒𝑎𝑟𝑠𝑡𝑎𝑟𝑡,𝑚𝑜𝑛)

𝑌𝑙𝑜𝑠𝑠 [kWh/kWp] = 𝐻𝑙𝑜𝑠𝑠 ∙ 𝑃𝑅𝑓𝑎𝑖𝑙

𝐸𝑙𝑜𝑠𝑠_𝑑𝑒𝑡𝑒𝑐𝑡𝑖𝑜𝑛 = 𝑌𝑙𝑜𝑠𝑠_𝑑𝑒𝑡𝑒𝑐𝑡𝑖𝑜𝑛 ∙  𝑃0 ∙ (

) ∙ 𝐶𝑃𝐿 ∙ 𝑀1

𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒 = 𝑌𝑙𝑜𝑠𝑠_𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒 ∙  𝑃0 ∙ (

) ∙ 𝐶𝑃𝐿 ∙ 𝑀1

𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑝𝑎𝑖𝑟 = (𝑌𝑙𝑜𝑠𝑠_𝑟𝑒𝑝𝑎𝑖𝑟 − 𝑌𝑙𝑜𝑠𝑠_𝑠ℎ𝑢𝑡𝑑𝑜𝑤𝑛) ∙  𝑃0 ∙ (

𝑛𝑓𝑎𝑖𝑙
𝑛𝑡𝑜𝑡𝑎𝑙

) ∙ 𝐶𝑃𝐿 ∙ 𝑀1

𝑛𝑓𝑎𝑖𝑙
𝑛𝑡𝑜𝑡𝑎𝑙
𝑛𝑓𝑎𝑖𝑙
𝑛𝑡𝑜𝑡𝑎𝑙

(2)

(3)

(4)

(5)

(6)

(7)

15

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

𝐸𝑙𝑜𝑠𝑠_𝑠ℎ𝑢𝑡𝑑𝑜𝑤𝑛 = 𝑌𝑙𝑜𝑠𝑠_𝑠ℎ𝑢𝑡𝑑𝑜𝑤𝑛 ∙  𝑃0 ∙ (

𝑛𝑓𝑎𝑖𝑙
𝑛𝑡𝑜𝑡𝑎𝑙

) ∙ 𝑀2

𝐸𝑙𝑜𝑠𝑠𝑇𝑂𝑇𝐴𝐿[kWh] =   𝐸𝑙𝑜𝑠𝑠_𝑑𝑒𝑡𝑒𝑐𝑡𝑖𝑜𝑛 +  𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒+𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑝𝑎𝑖𝑟 +   𝐸𝑙𝑜𝑠𝑠_𝑠ℎ𝑢𝑡𝑑𝑜𝑤𝑛

𝐶𝑑𝑜𝑤𝑛[€/kWp/year]   =

𝐸𝑙𝑜𝑠𝑠𝑇𝑂𝑇𝐴𝐿 ∗ 𝐹𝐼𝑇
𝑃0

𝐶𝑓𝑖𝑥 [€/kWp/year] =

(𝐶𝑑𝑒𝑡   +   𝐶𝑟𝑒𝑝/𝑠𝑢𝑏 +   𝐶𝑡𝑟𝑎𝑛𝑠 +   𝐶𝑙𝑎𝑏)𝑛𝑓𝑎𝑖𝑙
𝑃0

Where

Table 1: Parameter definition for calculating CPN.

(8)

(9)

(10)

(11)

𝑛𝑓𝑎𝑖𝑙

𝑛𝑡𝑜𝑡𝑎𝑙

Number of components affected

Total number of components

𝑃𝑅𝑓𝑎𝑖𝑙

𝑃𝑅𝑠𝑡𝑎𝑟𝑡,𝑚𝑜𝑛

𝑃𝐿𝑅

Performance Ratio when failure occurs [%]

Annual average PR calculated with the first

available complete year of monitoring data

[%]

Performance Loss Rate calculated using at

least two years of historical data [%/year]

𝑦𝑒𝑎𝑟𝑓𝑎𝑖𝑙

Year when failure occurs

𝐶𝑃𝐿

𝑀1

𝑦𝑒𝑎𝑟𝑠𝑡𝑎𝑟𝑡,𝑚𝑜𝑛  Year from which monitoring data is available  𝑀2

Component Power Loss [%]

Multiplier to consider failures that cause problems at

higher component level during detection, response

and repair times (excluding shutdown time) [--]

Multiplier to consider failures that cause problems at

higher component level during the shutdown time [--]

𝑌𝑙𝑜𝑠𝑠

𝐻𝑙𝑜𝑠𝑠

Specific Yield Loss, energy per kWp that the

plat would have produced if unaffected by

the failure [kWh/kWp]

Irradiation loss, calculated as the sum of

Plane of Array (POA) irradiation [kWh/m2]

𝐹𝐼𝑇

Feed in tariff [€/kWh]

𝐶𝑙𝑎𝑏𝑜𝑢𝑟  Cost of labour [€]

𝐸𝑙𝑜𝑠𝑠_𝑑𝑒𝑡𝑒𝑐𝑡𝑖𝑜𝑛  Energy loss during detection [kWh]

𝑡𝑟𝑒𝑝𝑎𝑖𝑟  Repair time [h]

𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒  Energy loss during response [kWh]

𝐸𝑙𝑜𝑠𝑠_𝑟𝑒𝑝𝑎𝑖𝑟

Energy loss during repair [kWh]

𝑛𝑆𝑇

𝐶𝑆𝑇

Number of site technicians involved in the repair activ-

ity

Internal cost (rate per hour) of the site technician [€/h]

𝐸𝑙𝑜𝑠𝑠_𝑠ℎ𝑢𝑡𝑑𝑜𝑤𝑛  Energy loss during shutdown [kWh]

𝐶𝑑𝑒𝑡𝑒𝑐𝑡  Cost of detection [€/component]

considerers CPL=100%

To account for various techniques (visual inspection,

Total energy loss [kWh]

IR for thermal anomalies, I-V curve tracing for power

deviations, EL for cracked cells, etc.)

𝐶𝑟𝑒𝑝𝑎𝑖𝑟   Cost of repair/substitution [€/component]

Total installed capacity of the PV plant [kWp]  𝐶𝑡𝑟𝑎𝑛𝑠𝑝   Cost of transportation [€/component]

𝐸𝑙𝑜𝑠𝑠𝑇𝑂𝑇𝐴𝐿
𝑃0

The CPN assesses the economic impact based on two factors: lost production during down-
time (Cdown) and costs related to fixing the issue at hand (Cfix).

Cdown  is  accurately  determined by  evaluating the  Performance Ratio (PR)  at the time  of the
failure’s appearance through the inclusion of the Performance Loss Rate (PLR). The PLR is
calculated using seasonal-trend decomposition using LOESS (STL) [31], which was selected

16

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

based on a comparative study of available algorithms [32]. This method decomposes a time-
series into its subparts and extracts a long-term trend of PR values. This trend is then subject
to linear regression and the PLR is given in percentage per year. By including the PLR, the PR
was derived for the time each failure occurred, instead of assuming a fixed PR value for all the
tickets for the whole period analysed.

For  the  calculation  of  the  initial  PR,  it  might  be  desirable  to  use  as  a  starting  point  the  PR
calculated right after the commissioning of the plant or even better, some months later, when
the modules' output power has stabilised.

The Component Power Loss (CPL) defines the power loss for the affected components of the
PV plant. The multipliers M1 and M2 ensure that components at higher component level, are
considered if needed. For example, a broken or stolen module affects the performance of the
whole string. The division into shutdown M2 and excluding shutdown time M1 is important as a
shutdown will affect not only one string but all strings which are connected to a combiner box
which is turned off, for instance to replace a module.

This development is a cornerstone for automating the CPN methodology for use with system
monitoring and maintenance ticket data of fleets of PV systems to gain qualitative as well as
quantitative insights into common performance issues of PV systems. An application example
follows in Chapter 4.1.1

2.3.2  Reliability, Availability and Maintainability (RAM) analysis

Technical risk and the reliability of a component are complements of each other, as long as
they cover the same sample space. In this context another widely used quantification method
is the Reliability, Availability and Maintainability analysis. RAM analysis aims to identify any
significant performance losses and then recommend improvements to the maintenance strat-
egy. In this bottom-up approach a Reliability Block Diagram (RBD) or the Fault Tree Analysis
(FTA) is recommended to determine the effects of the failure of individual components (Figure
5).

PV String

Start

PV String

PV String

Diode

Diode

Diode

Fuse

Fuse

Fuse

OR

Row Box

Central
Inverter

DCF

SPD

Combiner
Box

DC
Switch

IGBT

ACF

DCF

Fan

SMU

PV string

Module

gPV

Con

Cable

Figure  5:  Examples  of  Reliability  Block  Diagram  (TOP)  and  Fault  Tree  (BOTTOM).
Adapted from [11].

17

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

In RAM modelling, the reliability R is defined as the probability that a system or component
performs adequately within a given time.

∞

𝑅(𝑡) = ∫ 𝑓(𝑡)𝑑𝑡
𝑡

(12)

The probability density function PDF of failures f(t) with increasing lifetime is expressed by an
exponential, normal, Weibull or lognormal distribution. Weibull distributions are applicable to a
broad range of failure modes and mechanisms. The normal distribution is preferred for items
that  have  a  wear  out  mechanism  such  as  bearing  or  motors.  Derived  from  [33]  the  best-fit
PDFs for the different components are shown in Table 2.

Table 2: Best-fit PDFs for the components of a PV plant adapted from [33].

Component

PV modules

Bypass diode

DC switch

AC switch

AC circuit breaker

Connector

Inverter

PDF

Exponential

Weibull

Lognormal

Weibull

Weibull

Exponential

Lognormal

The failure rate 𝜆 is the frequency of component failure. The mean time to failure (MTTF) of a
component defines the expected life of non-repairable items.

𝜆 =

𝑓(𝑡)
𝑅(𝑡)

∞

𝑀𝑇𝑇𝐹 = ∫ 𝑅(𝑡)𝑑𝑡
0

(13)

(14)

Availability (A) is defined as the percentage of time that the plant was successfully operating.
A  is  MTTF  divided by the total  operating  time  and can  be  calculated  with  MTTF and Mean
Down time (MDT), as follows:

𝐴 =

𝑀𝑇𝑇𝐹
𝑀𝑇𝑇𝐹 + 𝑀𝐷𝑇

(15)

In [33], [11] and [34] the RAM analysis was performed based on failure rates taken from the
literature along with real data from PV systems’ operations over a 25 year period. The reliability
analysis has proven, that the expected lifetime of the PV modules records 44 years, whereas
the expected lifetime of the balance of system and inverter are 19 and 8 years respectively
[33]. In [11], the reliability of a string inverter is given between 8 (older devices) and 25 years
(state-of-the-art inverters). The associated reliability (after 20 years), availabilities and energy
losses are presented in Table 3.

18

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Table 3: Results of RAM analysis of a 15.3 MW PV plant adapted from [11].

Component

PV string

Combiner Box

Inverter

Transformer

Reliability
(after 20 years)

Availability

Energy Losses
[MWh]

88.7%

14.4%

0.1%

55.6%

99.85%

99.69%

99.42%

99.50%

805

1656

2842

2601

2.4  Risk Mitigation Measures

Once  technical  risk,  reliability  and  availability  have  been  determined,  mitigation  measures
(MM) can be assigned to reduce the associated energy losses. Jahn et al. [3] identified eight
generic mitigation measures for PV technical risk management:

•  Component testing of important plant components such as PV modules or inverters.
The testing can be performed by the manufacturer in the factory, or independent test-
ing at certified laboratory, or on‐site at the PV plant;

•  Design review and construction monitoring serve to catch issues caused by bad PV

plant design and poor PV construction workmanship;

•  EPC qualification focuses on ensuring the competencies of the field workers, e.g, by
requiring certain technical qualification prerequisites or regular training of the field
workers;
Implementing advanced monitoring system for early detection and diagnosis of
faults;

•

•  Use of basic monitoring system to monitor plant level alarms and notifications;
•  Advanced inspection (e. g., infrared thermographic or electroluminescence imaging)

to detect defects not usually visible to the naked eye;

•  Visual inspection to establish any visible changes in PV plant components;
•  Spare parts management to minimize the costs of downtime during repair or substi-

tution of components.

These MMs can be grouped into two main categories. Preventive measures are applied before
the failure occurs to prevent it from happening. The MMs under this category are component
testing, design review, construction monitoring, and EPC qualification. Corrective measures
are MMs that aim to reduce higher losses and costs if the failure has already occurred. Clean-
ing strategies to minimize soiling losses on the PV modules are described in [18]. The following
advanced inspection methods are presented in detail in [35].

•  Drone-mounted electroluminescence & thermal infrared imaging of PV arrays
•  Daylight I-V measurement of PV strings and PV modules
•  PV module characterization with mobile PV test centre
•  Dark I-V measurement of PV strings and PV modules
•  PV plant testing vehicle for PV strings
•  Electrical impedance spectroscopy of PV strings
•  Daylight electroluminescence imaging
•  UV fluorescence imaging
•  Advanced outdoor photoluminescence imaging of PV modules
•  Spectroscopic methods for polymeric materials

19

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

2.5  Best Practice, Limitations and Challenges

Choosing the best method for the individual purpose is rarely trivial. The advantages, and dis-
advantages of the presented methods are demonstrated considering the factors maturity level
and data availability and are illustrated in Figure 6.

FMEA  is  based  on the opinions  of  experts  defining  occurrence and  severity  of  events.  The
ranking within an FMEA is subjective and further use of RPNs, e.g. within a financial model, is
limited. It is usually applied during the early phase of the project, when new products or strat-
egies are implemented. It is best suited for immature technologies when operational data is
limited and no sufficient previous experience is available.

MCDA evaluates the performance of alternative courses of action. Its strong advantage is its
ability to capture both subjective and objective information, however weights and values are
difficult to estimate and it can results into skewness of results due to extreme values. It is best
suited for technologies at a relatively low maturity level where operational data and sufficient
previous experience is available.

CPN  assesses  the  economic  impact  based  on  factors  such  as  performance  reduction  and
down-time. It is based on statistical analysis and real-time data and can be applied to a single
PV plant or to a large portfolio of PV plants. It is best suited for technologies at a high level of
maturity where operational data and sufficient previous experience is available.

RAM analysis identifies significant causes of loss of availability or issues that limit the energy
yield. It starts during the early phase of the project and can be reviewed and updated as the
project progresses. It is best suited for mature technologies but in the case where operational
data is limited and insufficient previous experience is available, such as for young PV power
plants.

High Level
of Maturity

RAM

CPN

Low Data
Availability

High Data
Availability

FMEA

MCDA

Low Level
of Maturity

Figure 6: Selection guide of methods presented based on the driving-factors: data
availability and level of technology maturity.

20

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

  RISK DATABASE

According to the PMBOK guide [17], the Risk Database (RDB) is the central repository for all
information regarding the identified risks. In terms of technical risks the RDB provides the range
of affected components the description with causes and consequences, failure rates, the prob-
ability of occurrence, the impact on KPIs and the recommended control and mitigation actions.
It should be updated and maintained as a growing data hub through all phases of the project.
In this chapter we present a systematic approach to identify the main technical risks, define
the most important risk parameters and collect these failure, loss and occurrence data.

3.1  PV Failure Fact Sheets (PVFS)

The PV failure fact sheets (PVFS, Annex 1) summarise some of the most important aspects
of single failures. The target audience of these PVFSs are PV planners, installers, investors,
independent experts and insurance companies, and anyone interested in a brief description of
failures with examples, an estimation of risks and suggestions of how to intervene or prevent
these failures.

The failure sheets do not aim to deepen the theoretical background of the failures and its de-
tection, but they aim to summarise the key aspects described in the numerous IEA PVPS Task
13 technical reports [1] [16] [18] [36] [35] and reference documents [37] [38] [39] [40] [41] [42]
[43] [44] [45] [46] [47]  used for the  preparation of the  PVFSs  shown  in Table  4.  The failure
sheets are specific to the component in which they occur.

3.1.1  PVFS structure

The format of the PVFS is based on the failure description presented within the H2020 Solar
Bankability project [9]. A rating system for the estimation of the severity of a failure is used
here which simplifies the approach proposed within the IEA PVPS Task 13 [16] by implement-
ing  the  rating  system  proposed  by  the  Sinclairs  [37].  The  correlation  between  the  different
failures is highlighted in the text by using bold characters. Each PVFS is structured into 1 to 3
pages. The first page is a descriptive page, whereas the remaining pages contain examples
composed of a picture, a legend and an estimation about its severity. The first page is struc-
tured as follows:

Component

The PV system components are divided into:

(1)

(2)

(3)

(4)

PV module (including junction box)

Cables and interconnectors (at module, string and combiner box level)

Mounting (structure, clamps and screws)

Inverter

Defect

Short name describing the failure/defect.

Appearance

Description of how the defect looks like.

21

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Table 4: List of PV Failure Fact Sheets.

No

1-1

1-2

1-3

1-4

1-5

1-6

1-7

1-8

1-9

Component

PV module

PV module

PV module

PV module

PV module

PV module

PV module

PV module

PV module

1-10  PV module

1-11  PV module

1-12  PV module

1-13  PV module

1-14  PV module

1-15  PV module

1-16  PV module

1-17  PV module

1-18  PV module

1-19  PV module

1-20  PV module

Failure name

Cell cracks

Discolouration of encapsulant or backsheet

Front delamination

Backsheet delamination

Backsheet cracking

Backsheet chalking (whitening)

Burn marks

Glass breakage

Cell interconnection failure

Potential induced degradation

Metallisation discolouration/corrosion

Glass corrosion or abrasion

Defect or detached junction box

Junction box interconnection failure

Missing or insufficient bypass diode protection

Not conform power rating

Light induced degradation in c-Si modules

Insulation failure

Hot spot (thermal patterns)

Soiling

2-1

2-2

2-3

2-4

3-1

3-2

3-3

4-1

4-2

4-3

Cable and Interconnector

DC connector mismatch

Cable and Interconnector

Defect DC connector/cable

Cable and Interconnector

Insulation failure

Cable and Interconnector

Thermal damage in combiner box

Mounting

Mounting

Mounting

Inverter

Inverter

Inverter

Bad module clamping

Inappropriate/defect mounting structure

Module shading

Overheating (temperature derating)

Incorrect installation

Complete failure (not operating)

The list does not pretend to be exhaustive or updated. The complete list with all PVFS can be downloaded under
[48]

22

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Detection

Description of methods which can be used to detect the failure. Detection methods in brackets
lists secondary methods, which do not detect the failure with absolute certainty or which can
be used in addition to other methods. Following abbreviations are used:

Table 5: Abbreviations of Detection Methods.

Abbreviation

VI

IRT

EL

IV

UV

STM

MON

dIV

BYT

VOC

INS

Origin

Detection Methods

Visual inspection

Infrared thermography

Electroluminescence

Daylight I-V measurement

UV fluorescence

Signal transmission method

Data monitoring

Dark I-V measurement

Bypass diode testing

Voc measurement

Insulation testing

Description  of  the  failure  and  its  main  causes  and  origin  (1.  Material  and  production,  2.
Transport and installation, 3. Operation and maintenance).

Impact

Description of the impact on the safety, performance and reliability of the component and sys-
tem and its severity. For every failure, a range of possible ratings is given, one for the safety
and one for the performance.

A failure is defined as a safety failure when it endangers somebody who is applying or working
with PV modules or simply passing the PV modules. Three categories are defined in Figure 7.

Safety category

Description

Failure has no effect on safety.

Failure may cause a fire (f), electrical shock (e) or a physical dan-
ger (m) if a follow-up failure and/or a second failure occurs.

Failure can directly cause a fire (f), electrical shock (e) or a physi-
cal danger (m).

Figure 7: Safety category

23

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

A failure is defined as a performance failure when it impacts the performance and/or reliability
of a system. Five categories are defined in Figure 8. They go from 1 (low severity) to 5 (high
severity).

Performance category

Description

The defect has no direct effect on performance.

The defect has a minor impact on performance.

The defect has a moderate impact on performance.

The defect has a high impact on performance.

The defect has a catastrophic impact on performance.

Figure 8: Performance category

For each category, the expected loss is estimated on the component level and if no mitigation
measure is implemented. It can range from no power degradation (0%) over power degrada-
tion  below  detection  limit  (<2-3%),  power  degradation  within  warranty  (<0.7-1%/year)  and
power degradation out warranty (>0.7-1%/year) to catastrophic power degradation (>3%/year).

Mitigation

Description of the corrective actions to be done on a short and medium term when detecting a
failure and preventive actions to be implemented to avoid the failure from the beginning. Pre-
ventive actions are separated into recommended actions, representing the minimum require-
ment for small residential systems and optional actions for large scale systems.

The general rule for intervention in case of a failure is: All components with a direct safety risk
or  a  performance  severity  of  5,  highlighted  in  red,  should  be  replaced  or  repaired.  Regular
inspections should be performed to monitor the status of the not replaced or repaired compo-
nents.

3.1.2  Example PVFS: Front delamination

The delamination of the encapsulant FS1-3: Front delamination is here taken as example to
further explain the FS structure and rating system.

24

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure 9: First page of PVFS example with general information

25

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure 10: Remaining pages of a PVFS contain examples composed of a picture, a
legend and an estimation about its severity.

The first section of the sheet describes the appearance or how to recognise a specific failure
and  which  detection  methods  are  available.  Delamination  is  generally  easily  detectable  by
visual inspection (VI) of the modules from the front. Insulation measurements (INS) can give a
hint  of  a  severe  delamination,  but  it  is  not  the  first  method to  detect  an  early  delamination,
reason why it is put in brackets.

The second section describes the origin or in which phase of the lifetime of a PV system the
failure occurs and what the main causes are. Delamination problems have its origin mainly in
the quality of the raw material, the manufacturing process and/or the environmental factors to
which the modules are exposed during its operational lifetime.  Transport and installation do
not generate any delamination problems.

The third section describes the impact the failure has on the safety and performance of the
component and PV system. Below the general description the severity rating accord. Figure 7
and Figure 8 is given. The severity rating in the first page gives the full range of possible ratings
observable in the field and how the failure can evolve over the whole lifetime of a PV system.
The rating in the examples gives instead a snapshot of the gravity of the failure for a specific
case at a certain time. The pictures are taken from literature or case studies and give only a
partial picture of the situation and are here used to explain the potential levels of impact.

The delamination of the potting material does not automatically pose a safety risk. It is there-
fore  often  rated  as  not  critical  (see  example  1.3.1-1.3.7,  1.3.10  and  13.11  in  Annex  1),  but
depending on the propagation of the failure it can develop into a more severe safety failure.

26

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

When creating a continuous path between the electric circuit and the edge of the module (see
example 1.3.13-1.3.15), delamination can lead to electric leakage currents with a direct risk of
electrical shock or the risk can occur later, due to the progress of the delamination and/or the
ingress of moisture. This is particularly the case when the original delamination is close to the
edge of the module or the junction box, or if it is going over a very extended area (see example
1.3.8-1.3.12).  The  performance  loss  risk  for  modules  with  delamination  problems  ranges
from 1 to 5. Very small delamination areas on top of a cell or outside the cell area  and not
combined  with  other  failures,  are  classified  as  having  no  impact  (1)  or  a  minor  power  loss
typically below the detection limit (2), if the failure is not increasing over time (see example
1.3.1-1.3.4, 1.3.8, 1.3.10 and 1.3.11). The severity is in the range of (2-4) when the delamina-
tion area is getting larger (see example 1.3.7 and 1.3.9) or if it is occurring in combination with
follow-up failures like moisture ingress (see example 1.3.14) or an insulation failure (see ex-
ample 1.3.13). It increases also when occurring in combination with a second failure like dis-
coloration (yellowing or browning) of the encapsulant or backsheet (see example 1.3.6, 1.3.7,
1.3.13), or cell cracking (see example 1.3.5). A catastrophic performance loss of (5) is reached
when the cell mismatch is so large that one or more bypass diodes could be activated (see
example 1.3.13 and 1.3.14).

The  last  section  describes  the  mitigation  measures.  In  case  of  delamination,  all  modules
which do not guarantee anymore the electrical safety or insulation resistance or have an active
bypass diode, have to be replaced. Not replaced modules with minor delamination have to be
monitored by regular visual inspections and ground fault detection. Basic preventive measures
consist in selecting certified and tested products only. In case of large-scale systems regular
system inspection is recommended.

3.2  PV Failure Degradation Sheets (PVDS)

Besides the PVFS collection we provide an update on the statistical risk data of the PV Failure
Degradation  Sheet  (PVDS)  survey  developed  in  Koentges  et  al.  [1].  It  requires  much  more
detailed measured input data but it is able to generate statistical data on degradation rates and
power loss of PV systems based on failure types. Due to the high requirements on the PVDS
much less input data can be collected. In the following, we introduce the collected data, the
way of analysing the data and the analysis results.

3.2.1  Introduction of PVDS

The failure data is collected in an excel sheet which is sent to system owner, experts installer
or manufacturer. Some data is also collected by scientific publications or an Australian internet
survey. The survey structure is first presented in the IEA PVPS TASK 13 report “Assessment
of Photovoltaic Module Failures in the Field” [1], see also Figure 11. The plain survey and the
survey  explanation  can be  downloaded  here [49]  [47].  The  survey  is  structured  into system
components, as described in Chapter 3.1. All system components may have various prede-
fined failures. For each failure, a power loss and a safety failure may be given. Furthermore,
for each system a Koeppen-Geiger climate zone must be selected. The Koeppen-Geiger cli-
mate zones shift during the ongoing climate change. We used the Koeppen-Geiger map cal-
culated by Rubel [50] for the time period 1976-2000 as classification classes.

Compared to the first presented survey structure in [1], we added two new failure categories
for PV modules: LID/LeTID degradation and potential induced delamination [51]. Furthermore,
it  is  now  possible  to  add  all  three  letters  of the  Koeppen-Geiger  classification  to the  survey
compared to one in the first version. The translation tool for “geo data” to “Koeppen-Geiger
climate zones” [52] helps to find the correct classification for each position in the world.

27

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure 11: Top rows of the PVDS excel sheet for the failure collection. The symbols
in the fields illustrate the source of the data for the calculation of degradation values.
For the sake of clarity, only indicated here for the evaluation of module failures.

3.2.2  Introduction of statistical evaluation

The calculation of basic degradation values is done as described in [15]. Table 6 lists all cal-
culated  basic  degradation  values  and  input  variables.  Figure  11  shows  the  corresponding
value sources of the data in the excel sheet.

Table 6: Description and calculation of degradation values from input values of the
PVDS survey.

Description of value

Symbol  Unit

Calculation or source of value

Data number

Failure specification for
system part k in system i

Failure type

Nominal power of a sys-
tem i

By failure x affected sys-
tem part of system i for
part k of the system

i

k

x

Pi

zi,x,k

By failure x affected sys-
tem part of system i

zi,x

28

Anonymized iteration number of
data “System ID”

There are 5 sections in the data
sheet were a failure can be
specified. “k” is the iteration
number of the section.

Data “Failure specification”

kWp

Data “Nominal system power”

% of the total
nominal system
power

Data “Failure specification for ”
_% “of the system” for part k of
the system i

% of the total
nominal system
power

z𝑖,x =∑z𝑖,x,k
Sum over all sections k having
an entry for failure x

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

System part of system i
being analysed for fail-
ures. System parts are
given for the system
components: Inverter,
Cable and intercon-
nector, PV modules,
mounting and other sys-
tem components

Power loss for a speci-
fied failure x in system I
for part k of the system

Date of the failure docu-
mentation

Commissioning date of
system

Number of x type failures
in the survey.

Mean power loss for a
specified failure x in sys-
tem i.

Degradation rate of a
specific module failure
type x of dataset i.

Degradation rate of the
whole system for the fail-
ure type x for dataset i. It
is expected that the in-
vestigated part of the
system is representative
for the whole system.

Mean degradation rate of
a specific module failure
type x.

Number of datasets i
with the failure type x in
the whole dataset or in a
specific part of the data
set (e.g., restricted to a
climate zone).

yi

% of the total
nominal system
power

Data given in “Following failure
specifications are based on in-
vestigated percentage of” for
each system component

ΔPi,x,k

% of the nomi-
nal component
power

Data given in “Power loss 1” or
“Power loss 2“ for a failure x in
system I for part k in the system

Τb,i

Τa,i

nx

Δ𝑖,𝑥

di,x

δi,x

𝑑̅𝑥

nx

date

data

Data “Date of failure docu-
mented here”

Data “Date of system start”

nx amount of systems in the sur-
vey with the failure x

Δ𝑖,𝑥=∑ ΔP𝑖,𝑥,k*zi,x,k/zi,x
Sum over all sections k in data
set i having an entry for failure x

di,x= Δ𝑖,𝑥 /(𝜏𝑏,𝑖−𝜏𝑎,𝑖)

δi,x= 𝑑𝑖,𝑥zi,x/𝑦𝑖

% of the nomi-
nal power of the
investigated
system part

% of the nomi-
nal power of the
investigated
system part

% of the nomi-
nal power of the
investigated
system

𝑑̅𝑥=∑𝑑𝑖,𝑥/𝑛𝑥

% of the nomi-
nal power of the
investigated
system part

nx=∑f(i,x)
 with f(i,x)=1 if dataset has an
documented failure x,
otherwise, f(i,x)=0

Mean degradation rate of
the whole system for the
failure type x.

𝛿̅𝑥

𝛿̅𝑥=∑𝛿𝑖,𝑥/𝑛𝑥

% of the nomi-
nal power of the
investigated
system

29

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

𝑝𝑖,𝑥

𝜋𝑖,𝑥

Percent of the investi-
gated system power pi,x
affected by a power loss
after a sudden event x
for system i. It is ex-
pected that the investi-
gated part of the system
is representative for the
whole system.

Power loss relative to the
investigated system
power. It is expected that
the investigated part of
the system is repre-
sentative for the whole
system.

𝑝𝑖,𝑥=𝑧𝑖,𝑥/𝑦𝑖

% of the investi-
gated system
equivalent to
% of the total
system

𝜋𝑖,𝑥= Δ𝑖,𝑥 𝑝𝑖,𝑥

% of the power
of the investi-
gated system
equivalent to
% of the power
of the total sys-
tem

The  evaluation  of  the  failure  date  is  based  on  several  assumptions.  It  is  assumed  that  the
person who documented a failure in the database analysed a representative part of  the PV
system. Therefore, we assume that we can extrapolate the failure impact x of the investigate
system part (yi) to the total system (Pi). The data are stored in monthly resolution in the data-
base. The analysis is done on a yearly resolution. Failures occurring in the first year of system
power production are categorised into year 1 and so on for the following years of operation.
We do not know the progress of most of the failures with time. However, many studies show
that especially module-based failures proceed somewhat linearly. Therefore, we calculate deg-
radation rates from the database with the assumption that the power degrades linearly (di,x,δi,x
and the respective mean values) with time. Furthermore, there are failures which are expected
to be sudden events. In this case we calculate the system part which is affected by the failure
(𝑝𝑖,, 𝑥) and the resulting power loss relative to the total system power (𝜋𝑖,𝑥, 𝑥) and their corre-
sponding mean values. The following listings shows to which power loss categories the failure
types are assigned.

Linear degradation profile: Delamination, defect backsheet, defect junction box, junction box
detached, frame breakage/bown/defect, discolouring of pottant, cell cracks, burn marks, po-
tential induced shunts (often named PID), potential induced corrosion (often with thin-film mod-
ules), potential induced delamination, LID/LeTID degradation, disconnected cell or string inter-
connect ribbon, defective bypass diode/wrong dimensioned, corrosion/abrasion of AR coating,
isolation failure, CdTe: back contact degradation

Sudden power loss: Glass breakage, hail -> glass breakage/cell breakage, snow load -> de-
formed  frame/glass-  /cell-breakage,  Storm  ->  deformed  frame/glass-/cell-breakage,  direct
lightning stroke -> defect glass/frame and defect bypass diodes, animal -> bite/corrosion/dirt,
biofilm soiling, dust soiling

3.2.3  Results of new failure data evaluation

Unfortunately, many datasets were not complete so that we had to exclude a lot of data. Since
the last failure data evaluation [1], we added 76 new complete PVDSs to the PV system data
collection. The data collection consists of 226 PVDSs in total. An overview of the distribution
of the PV systems and the analysed PV module technologies is given in Figure 12. Most data
is from Europe. In total, data from all 6 continents are available. Although the market share of

30

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

mono- and multi-crystalline silicon solar wafers has switched from the multi market domination
to a mono market domination, the main analysed technologies are still multi-crystalline silicon
wafer based solar cells. In the data collection, PV systems are include with installation year
beginning from 1982 to 2018. Over 90% of the data are from PV systems installed in the range
of 2005 to 2018.

Figure 12: Left - Distribution of PV system locations in the data collection.
Right - Distribution of PV module technologies in the data collection.

Figure 12 shows the frequency distribution for PV module failures with an impact on the power
generation of the PV systems. The distribution is split into failures which lead to a degradation
and sudden occurring failures. Most reports on failures with power loss are given in the first 10
years of operating time. This is to be expected as it is often too expensive to repair PV systems
older than 10 years. Therefore, no detailed analysis is made. The main results of the last report
“Assessment of Photovoltaic Module Failures in the Field” remain true. PID effects, cell cracks
and  defective  bypass  diode  failures  seem  to  dominate the  failure  statistic  in  the  first  seven
years. This dominance now becomes even more pronounced in comparison with the statistics
presented  in  [1].  Additionally,  the  failure  type  “burn  marks”  have  been  detected  more  fre-
quently. For sudden events, also shown in Figure 13, the failure glass breakage and dust soil-
ing fully dominate the failure statistic.

Figure 14 shows the power loss impact of sudden events on PV system performance. Docu-
mented glass breakage events lead in temperate climates to a loss of 1% to 2% of a system's
power, with one exception in the dataset. These events seem to occur everywhere but appear
to be not so severe for the whole system. Dust soiling appears everywhere except for tropical
climates.  In  temperate  climates,  the  impact  is  at  a  maximum  7%  of  the  total  system  power
whereas up to 15% power loss occurs in dry climates and over 25% for continental climates.
As expected, the deformed PV module frame due to snow load occurs only in the continental
and polar climate.

31

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure  13:  Failure  frequency  for  PV  module  defects  with  an  impact  on  the  system
power. The upper graph is showing PV module failure frequency with a slow degrada-
tion over time and the lower graph failure frequency for sudden events.

Figure 14: Power loss of sudden failure events on the total power of the PV system.

32

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure 15 and Figure 16 show the degradation rate for the affected system parts and the whole
system for various failures sorted by climatic zones. The additional data supports the former
statements for the degradation rates of the failure types in [1].

Figure 15: Box plot of degradation rates dx of PV module affected by failures x sorted
by climatic zones. The numbers show the quantity of data per failure in the database.
The cross shows the mean degradation rate. The boxes include 50% of all values, the
whisker show the full range of existing values. The middle line in the box shows the
median.

Figure 16: Degradation rates of the whole PV system sorted by climatic zones. The
numbers show the quantity of data per failure in the database. The boxplot and the
whisker have the same meaning as in Figure 15.

33

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Figure 17: Left - Failure frequency of PID-s. Right – Burn mark cases in the base data
as function of the installation time of the system.

A common effect is that new and unexpected failures types occur in the field. After they are
recognised, understood and tests are developed, the failure type vanishes in the field because
the manufacture can develop their products defect free. The PID-s and burn mark effect, shown
in Figure 17, are good example for such a cycle. The first PID-s reports are for PV systems
installed in 2008. In 2016, after 8 years, we have no more reports on PID-s failures in the field
in the data collection. The burn mark defects show a similar trend.

However, for new PV modules similar failure types may reappear in the field. A potential in-
duced  polarization  (PID-p)  effect  is  found  for  PERC  solar  modules  with  bifacial  cell  design
(PERC+) [53]. However, this effect was found before large systems have been installed. Sim-
ilarly, we have observed hot cell effects in PV modules with high power (>400 Wp) [54]. Per-
fectly blocked cells in high power modules, when locally shaded, may become as hot as about
180°C in the full unshaded cell area. However, this effect is found in an early stage to develop
mitigation strategies before these modules were installed in the field.

There are some substantial types of PV module failures missing in the PVDS which have a
major  impact  on  power  loss for  PV  systems  if  they appear. We could not manage to fit the
available data into the data collection as always, some important data is missing, there are
reports on acetic acid corrosion focussing on tropical climates [55] which led to power losses
between 30% to 70% of the PV modules in 8 years of exposure. This defect type does not
occur in the same time span with the same module type in moderate climates. Furthermore,
there  are  reports  on  back  sheet  failure  causing  some  isolation  failures  up  to  corrosion  and
power loss in the solar cell matrix of the modules [56], [57] up to a total loss of mechanical
module integrity with a following disintegration of the modules.

34

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

3.3  PV Cost Data

Besides the power of the PV system, occurring costs are essential to make the best decisions
from  a cost-benefit  perspective.  O&M  costs  are  costs  required  to  operate  and maintain  PV
plants. The scope of O&M works comprises of tasks such as IR scans of the plant as intro-
duced in Chapter 2.4, and supports the identification of performance losses. Therefore, these
costs are part of the quantitative risk assessment. For the most important measures the cost
ranges were collected from [19] and are shown in Table 7.

Table 7: Collection of typical costs for individual O&M services [19].

PM Task

Costs

Remarks

Base O&M scope

6 - 14 €/kWp/year

Cleaning/washing
of PV modules

0.5 - 2.5 €/kWp/year

IR scans

0.5 – 3.0 €/module

EL scans

3.0 – 10.0 €/module

Includes: full preventive maintenance
scope, regular module cleanings, security
(remote or on-site); excl. IR and EL scans.
Varying highly with the site characteristics,
labour and frequency of activity.

Varying with the module technology, labour,
cleaning solution and method, climatic con-
ditions (affecting the frequency), etc.

Includes drone inspections, analysis and re-
porting

35

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

  CASE STUDIES

Having the methods presented and data collected, the following chapter demonstrates risk and
cost-benefit analysis using three case studies that show techniques for prioritising decisions
from an economic perspective and provide important results for risk managing strategies.

4.1  Risk Analysis

Risk analysis enables users with statistical and reliability data to develop and run scenarios in
which PV performance and costs are affected by components that can fail.

4.1.1  Case 1: Inverter complete failure (not operating)

In this chapter the revised CPN approach, introduced in Chapter 2.3.1 is presented through an
exemplary calculation of individual CPN values [4] [58].

The  PV  plant  under  consideration  is  in  operation  since  2013  and  is  located  in  central  Italy.
Table 8 summarizes the metadata of the system.

Table 8: Metadata of investigated PV plant in Case 1.

Parameter

Type of plant

Ground-mounted fixed tilt

Installed capacity

9,019.531 kWp

Country

Italy

Commissioning data

25-08-2013

Feed in tariff

0.119 €/kWh

Number of modules

69,381

Module nominal power

130 Wp

Number of inverters

17

Inverter nominal power

500 kW

Overall, 191 maintenance tickets were analysed manually, corresponding to all the planned
and corrective activities carried out in 2018 for the example plant. Time-series of monitoring
data are available since November 2016, including on-site irradiance (pyranometer measure-
ments) and power (inverter measurements). A detailed metadata table was created containing
all the relevant parameters useful for our purpose, mapping all the components of the plant
whose failure could cause a power loss. This metadata table was populated using as source
the available as-built documentation, the O&M contract and other CAPEX and OPEX related
documents.

The  improved  CPN  methodology  has  been  applied  manually  to  the  introduced  case  study,
which led to important improvements, especially in terms of the structure and standardisation
of the CPN table (see Table 9). The analysis of real maintenance tickets has mainly led to the
optimization of the number and format of the input parameters. Instead of using the methodol-
ogy  to  create  scenarios  based  on  assumptions  that  would  cover  a  wide  spectrum  of  O&M
approaches, real data from a specific O&M contractor were used. Parameters such as costs
of interventions and spare parts, failure, acknowledgement, response and repair times were
directly extracted from the monitoring and ticketing system. This task proved to be very time-
consuming because, although the description of failure and corrective measures is common

36

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

practice in the field of O&M, it is not often carried out with the sufficient level of detail to derive
meaningful statistical analyses due to the lack of a standardized approach in the assignment,
wording and categorization of failures.

Table 9: Extract of the CPN table related to the Case 1.

Ticket name

tdetection

tresponse

trepair

ElossTOTAL

Cfix

Cdown

CPN

[h]

[h]

[h]

[kWh]

[€]

[€/kWp]

[€]

[€/kWp]

[€/kWp]

Inverter 3D off

0.40

0.10

1.33

424

50.44

0.01

46.67

0.005

0.011

Meter 1 con-

nect error

18.20

1.00

95.5

0

0.0

0.00

255.00

0.028

0.028

Inverter 1B off

2.60

126.15

502.83

27,956

3,326.7

0.37

1,066.00

0.118

0.487

Inverter 1B off

1.18

0.40

0.58

76

9.09

0.00

20.42

0.002

0.003

Inverters cabin

3 off

8.70

16.30

0.83

4,704

559.83

0.06

29.17

0.003

0.065

Inverter 1B off

1.58

Plant off

0.17

1.00

0.17

8.17

2,326

276.73

0.03

285.83

0.032

0.062

19.83

11,360

1,351.86

0.15

35.00

0.004

0.154

The results presented in Table 9 are examples of how the CPN methodology can be used to
accurately  calculate  the cost  of  individual  entries  in the  ticketing  system of  a  PV  plant.  The
automation of calculating the CPN for a great number of tickets and plants will enhance our
understanding  of  the  appearance  likeliness  and  severity  of  PV  plant  performance  impairing
issues in order to improve the operation of existing plants and the design of future PV systems.
It is concluded that the development of an automated and therefore, time-efficient solution for
extracting key parameters from maintenance tickets is of vital importance for the implementa-
tion of the methodology at portfolio level, and thus, to gain statistical insights from the large
number of PV plants.

It became apparent that the O&M field practices must move away from the manual input of
tickets in text format and adopt a more standardised approach where human intervention is
limited to choosing the category and failure type from a pre-defined selection list.

4.1.2  Case 2: PV Module PID

How  the  risk  quantification  method  can  be  also applied  in practice  is  demonstrated  using  a
10 MW PV plant with PID affected PV modules. The assumptions in Table 10 serve as input
for this case study. Not considered are financial parameter as depreciation, interest or taxes.

Table 10: Metadata of investigated PV plant in Case 2.

Parameter

Risk

Detection time

Response time

Repair time

Size of plant

Potential induced degradation (PID)

4 years

1 year

1 year

10 MW

Module tilted/ orientation

20°, 0° south oriented, 2 portraits

Type of installation

Free Field Installation

37

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Base frame

Modules

Inverters

PPA

CAPEX

OPEX

Inverter nominal power

Fixed Installation

40000 x 250 Wp

20 x 500 kVA

0.25 €/kWh

20 Mio€

50 k€/a

500 kW

Taking the behaviour of the identified root cause into account, the potential future PLR is ex-
pected to increase further with an expected saturation of 50%. After this value is reached, the
PLR is expected to stagnate at a constant level of 0.7% per year. This prediction of perfor-
mance development for 20 years of operation is shown together with the exceedance proba-
bility P10 and P90 for a confidence level of 68.2% in Figure 18. Taking CAPEX, OPEX and
annual revenues into account, the project’s financial profit after 20 years of operation is 48%
below original expectations for the defined scenario without mitigating actions.

Figure 18: Energy forecast of No-Mitigation Scenario.

4.2  Cost-Benefit Analysis

The CPN methodology allows the estimation of the economic impact of failures on the LCOE
and on  business  models  of  PV  projects  and  has  been  developed  not  only  to  determine the
economic impact of technical risks, but also to be able to assess the effectiveness of mitigation
measures. Specific failures have to be examined in order to draw recommendations on how to
mitigate the economic impact for, e.g. soiling, or potential induced degradation (PID). Some
failures can be prevented or mitigated through specific actions at different project phases (e.g.
for PID); others (e.g. soiling) can be prevented or mitigated through a more generic action. For

38

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

example,  the  monitoring  of  performance  or  visual  inspection  can  be  considered  as  generic
mitigation  measures  that  can  have  a  positive  impact  on  the  reduction  of  the  CPN  of  many
failures. In practice, it is important to understand how mitigation measures can be considered
as a whole to be able to calculate their impact and thus assess their effectiveness.

4.2.1  Case 2: PV Module PID

The cost-benefit analysis is also a tool to determine whether the benefit of one option will justify
its  costs.  It  can  point  out  the  best  mitigation  options from  an  economical  point  of  view.  The
analysis continues the case study presented in Chapter 4.1.2. Three mitigation scenarios are
defined:

•  No-Mitigation option without intervening into the current status of plant operation
•  PID Box: Installing PID-boxes and allowing the performance of the PV modules to re-

cover to a certain level

•  PID Box & partial repowering: Installing PID-boxes and replacing very low perform-

ing PV modules by high-power-modules.

The  expected  annual  production  of  energy  yields  for  the  three  scenarios  is  illustrated  in  in
Figure 19. After the mitigation measures were applied in year 5 of the operation, the energy
yields show a steep rise. The expected PV plant output after 20 years of operation is calculated
at 45% rated energy output for the no-mitigation scenario and at 84% and 91% for mitigation
options 1 and 2, respectively.

e
m

i
t
n
o
i
t
c
e
t
e
D

e
m

i
t
e
s
n
o
p
s
e
R

e
m

i
t

r
i
a
p
e
R

Figure 19: 20-year forecast for three mitigation scenarios; the repowering is carried out
with a higher module power class.

39

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Table 11: Costs of mitigation scenarios.

No-Mitigation

PID Box

PID Box & partial repowering

Cost [k€]

15

238

3233

The cost-benefit analysis also takes the associated costs of the available options into account,
as described in Table 14. The impact on the annual cash flow is demonstrated in Figure 20. In
the reference scenario, the monetary yield of the PV project after 20 years is expected to be
around  225%  of  the  CAPEX  (dashed  line).  If  no  mitigation  measures  are  taken,  the  lowest
result of around 115% of CAPEX is forecasted. Mitigation options 1 and 2 result in 6.0%, re-
spectively 4.6% below expectations, which both represent successful projects results. It can
be concluded that both mitigation options should be considered and taken as a solution com-
pared to non-action. However, the additional investments in year 5 of operation for option 2
are significantly higher by a factor of 8.

CPN (5years) = 151€/kWp
Revenue Loss = 1.51Mio€
7.6% of investment

CPN (10years) = 745€/kWp
Revenue Loss = 7.45Mio€
37.3% of investment

Figure 20: Annual cumulative cash flow of the mitigation scenarios with CPN and loss
of revenue after 5 and 10 year of operation if no action is taken.

4.2.2  Case 3: PV Module Soiling

Cleaning routines for PV power systems in desert regions are a typical corrective measure to
reduce energy yield losses due to soiling. The impact of different cleaning procedures on the
soiling losses over one year are calculated and shown in Figure 21 for a 10 MWp PV plant
near Abu Dhabi [59]. The soiling rate is 0.3%/day and only two significant precipitation events
are  recorded  during  one  year.  If  no  cleaning  (natural  cleaning)  is  performed,  soiling  losses
(brown bars) may reach up to 30% per year and result in annual costs of 2614 k$ (Table 12).

40

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

Table 12: Impact of cleaning routines on soiling losses of a 10 MWp plant in Abu Dhabi.

Index

Soiling Loss

Precipitation Events

Cleaning Events

Natural Cleaning

Periodic Cleaning

Triggered Cleaning

[%]

28.4

4.1

2.3

[-]

2

2

2

[-]

0

12

20

In case of periodic cleaning (monthly cleaning), energy losses due to soiling are reduced to
4% (green bars) resulting in reduced yield losses (377 k$) and an annual cost of 497 k$, which
includes the costs of the 12 cleaning routines (Table 12). Best economic cleaning measure is
achieved when performing “triggered cleaning” at a soiling loss of 5%, which results in further
reduced yield losses (212 k$) and an annual cost of only 412 k$, which includes the costs of
20 required cleaning routines (Table 12). The calculations show that it is possible to determine
the best economic solution for a specific PV plant (10 MWp), location (Abu Dhabi), loss sce-
nario (0.3%/day soiling loss rate) and mitigation concept (three types of cleaning).

Table 13: Impact of cleaning routines on monetarized yield losses of a 10 MWp plant in
Abu Dhabi.

Index

Yield Loss

Cleaning Cost

Total Cost

Natural Cleaning

Periodic Cleaning

Triggered Cleaning

[k$]

2614

377

212

[k$]

0

120

200

[k$]

2614

497

412

Figure 21: Impact of cleaning routines on soiling losses of a 10 MWp plant in Abu Dhabi.

41

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

  CONCLUSIONS

Best practice guidelines to improve the operation of PV power systems are often only applied
as  long  as  recommended  actions  have  advantages  for  the  executors,  the  EPCs  and  O&M
companies and for the investors whose main focus is on low risks and maximum profit from an
economic point of view. This leads to the key challenge: How can you demonstrate the effec-
tiveness of the measures and justify their application? The technical best solution is not always
the economically best one. Before you are able to evaluate the cost-benefit, the following ques-
tion arises: How to quantify the basic impact of technical risks?

In order to answer these questions, we introduced semi-quantitative and quantitative method-
ologies to assess technical risks in PV power systems and provided 30 examples of common
technical risks described and rated in the new created PV failure fact sheets (PVFS). Besides
the PVFSs based on expert knowledge and expert opinion, an update on the statistics of the
PV failure degradation survey developed in Koentges et al. [1], was given. With the knowledge
acquired  and  data  collected,  the  risk  and  cost-benefit  analysis  were  demonstrated  in  three
case studies that showed methods for prioritising decisions from an economic perspective and
provided important results for risk managing strategies.

However, providing the overview of quantification methods, we draw the conclusion that more
standardisation is required. Risk definitions are not fully structured and event databases (solar
logbooks)  are  not  harmonised.  Data  analysis  would  benefit  from  the  use  of  a  standardised
language and  metadata formats.  Development  of  an  automated  and  therefore  time-efficient
solution for extracting key parameters from maintenance tickets is required to gain statistical
insights from a large number of PV plants. Also, the development of a software tool for field
technicians is recommended that would allow the precise and error-free recording of standard-
ised  parameters  for  the  calculation  of  the  O&M  contractors  KPIs  necessary  for  an  efficient
implementation  of the methodology [4]. In  summary,  the O&M  field practices must  certainly
move away from a manual input of tickets in text format and adopt a more standardised ap-
proach where human intervention is limited.

In the 2020 launched H2020 project TRUST-PV [60], the improved Cost Priority Number ap-
proach is the basis for the creation of a large database including PV system data, coming from
several major O&M companies and asset managers across Europe, for failure rates calcula-
tion. It is thereby a direct continuation where the improved Cost Priority Number methodology
will be automatised in terms of acquiring failure data, power loss calculations and related cost
determination. The output will later be integrated in the PV plant design of newly commissioned
PV plants and in a decision support system platform for operating plants.

Technical risks from a reliability perspective, as introduced in the RAM analysis, are addressed
in IEC TS 63265 – “Reliability practices for the operation of photovoltaic power systems”, co-
ordinated by Roger Hill with the planned publication in the first half of 2022. Its motivation is to
provide a toolkit description of many methods of how different stakeholders can demonstrate
the effective of reliability increasing measures from technical and economic point of view.

All things considered, we believe that data-driven evaluation of techno-economic performance
indicators is a significant key to take decision support on LCOE to the next level.

42

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

REFERENCES

[1]   M. Köntges, G. Oreski, U. Jahn, M. Herz, P. Hacke, K. A. Weiss, G. Razongles, M. Paggi, D. Parlevliet, T.
Tanahashi and R. H. French, Assessment of Photovoltaic Module Failures in the Field, Report IEA-PVPS
T13-09: ISBN 978-3-906042-54-1, 2017.

[2]   D. Moser, M. D. Buono, U. Jahn, M. Herz, M. Richter, and K. D. Brabandere, “Identification of technical risks
in the photovoltaic value chain and quantification of the economic impact,”, Progress in Photovoltaics:
Research and Applications, vol. 25, no. 7, pp. 592–604, 2017, doi: 10.1002/pip.2857.

[3]   U. Jahn, M. Herz, D. Moser, G. Belluardo and M. Richter, Managing technical risks in PV investments: How
to quantify the impact of risk mitigation measures for different PV project phases?, Prog Photovolt Res Appl.
2018; 26: 597– 607. https://doi.org/10.1002/pip.2970.

[4]   G. Oviedo Hernández, S. Lindig, D. Moser, and P. V. Chiantore, "Optimization of the Cost Priority Number
(CPN) Methodology to the Needs of a Large O&M Operator," in 36th EUPVSEC Proceed-ings, Sep. 2019,
pp. 1613 - 1617.

[5]   C. M. Spencer, S. J. Rhee, Cost based failure modes and effects analysis (FMEA) for systems of

accelerator magnets, in Pro-ceedings of the 2003 Particle Accelerator Conference, 2003, vol. 4, pp. 2177–
2179 vol.4, doi: 10.1109/PAC.2003.1289057.

[6]   W. Gilchrist, Modelling Failure Modes and Effects Analysis. Int J Qual Reliab Manag, 1993, 10:16–23. doi:

10.1108/02656719310040105.

[7]   A. Hassan, I. Dayarian, A. Siadat, J.-Y. Dantan, Cost-based FMEA and ABC concepts for manufacturing

process plan evaluation, in 2008 IEEE Con-ference on Cybernetics and Intelligent Systems, 2008, pp. 197–
202, doi: 10.1109/ICCIS.2008.4670795.

[8]   M. Shafiee, F. Dinmohammadi, [Accessed: 09-Jun-2021], An FMEA-Based Risk Assessment Approach for
Wind Turbine Systems: A Comparative Study of Onshore and Offshore, Energies, vol. 7, no. 2, pp. 619–
642, Feb. 2014, doi: 10.3390/en7020619. [Online]. Available: https://www.mdpi.com/1996-1073/7/2/619.

[9]   "Solar Bankability project website," accessed: 2020-04-28. [Online]. Available:

http://www.solarbankability.org/home.html.

[10]  S. Kurtz, K Whitfield, N. Philips, T Sample, C. Monokroussos, E. Hsi, I. Repins, P. Hacke, D. Jordan, J.
Wohlgemuth, P. Seidel, U. Jahn, M. Kempe, T. Tanahashi, Y Chen, B. Jaeckel and M. Yamamichi,
Qualification testing versus quantitative reliability testing of PV – Gaining confidence in a rapidly changing
technology: European Photovoltaic Solar Energy Conference and Exhibition, 25-29 September 2017, RAI
Convention and Exhibition Centre, Amsterdam, The Netherlands, EU PVSEC conference proceedings,
2017, ISBN 3-936338-47-7, ISSN 2196-100X, p. 1302 - 1311, JRC107895.

[11]  S. Baschel, E. Koubli, J Roy, R. Gottschalg. Impact of Component Reliability on Large Scale Photovoltaic

Systems’ Performance. Energies. 2018; 11(6):1579. https://doi.org/10.3390/en11061579.

[12]  D. Moser, S. Lindig, M. Richter, J. Ascencio-Vásquez, I. Horvath, B. Müller, M. Green, J. Vedde, M. Herz, B.
Herteleer, K.-A. Weiss, B. Strindh, Uncertainty in Yield Assessments and PV LCOE, Report IEA-PVPS T13-
18, ISBN 978-3-907281-06-2, 2020.

43

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

[13]  S. Lindig, D. Moser, A. J. Curran, K. Rath, A. Khalilnejad, R. H. French, M. Herz, B. Müller, G. Ma-krides, G.

Georghiou, A. Livera, M. Richter, J. Ascencio‐Vásquez, M. van Iseghem, M. Meftah, D. Jordan, C. Deline,
W. van Sark, J. S. Stein, M. Theristis, Progress in Photovoltaics: Research and Applications, vol. n/a, no.
n/a, 2021, doi: https://doi.org/10.1002/pip.3397. [Online]. Available:
https://onlinelibrary.wiley.com/doi/abs/10.1002/pip.3397. [Accessed: 26-Mar-2021], B. Meyers, F.
Baumgartner, and W. Luo, “International collaboration framework for the calculation of performance loss
rates: Data quality, benchmarks, and trends (towards a uniform methodology).

[14]  R. H. French, L. S. Bruckman, D. Moser, S. Lindig, M. v. Iseghem, B. Müller, J. S. Stein, M. Richter, M.

Herz, W. v. Sark, F. Baumgartner, Assessment of Performance Loss Rate of PV Power Systems, Report
IEA-PVPS T13-22, ISBN 978-3-907281-10-9, 2020.

[15]  M. Richter, C. Tjengdrawira, J. Vedde, L. Frearson, B. Herteleer, M. Green, B. Stridh, U. Jahn, M. Herz and

M. Köntges, Technical Assumptions Used in PV Financial Models - Review of Current Practices and
Recommendations, Report IEA-PVPS T13-08: ISBN 978-3-906042-46-6, 2017.

[16]  M. Köntges, S. Kurtz, C. Packard, U. Jahn, K. A. Berger, K. Kato, T. Friesen, H. Liu, M. Van Iseghem, J.

Wohlgemuth, D. Miller, M. Kempe, P. Hacke, F. Reil, N. Bogdanski, W. Herrmann, C. Buerhop Lutz and G.
Friesen, Review of Failures of Photovoltaic Modules, Report IEA-PVPS T13-01: ISBN 978-3-906042-16-9,
2014.

[17]  Project Management Institute. (2017). A guide to the Project Management Body of Knowledge (PMBOK

guide) (6th ed.). Project Management Institute.

[18]  C. Schill, D. Parlevliet, A. Anderson, B. Stridh, L. Burnham, C. Baldus-Jeursen, L. Micheli, E. Urrejola, E.

Whitney and G. Mathiak, Soiling Losses – Impact on the Performance of Photovoltaic Power Plants, Report
IEA-PVPS T13-21: ISBN 978-3-907281-09-3, 2021.

[19]  U. Jahn, B. Herteleer, C. Tjengdrawira, I. Tsanakas, M. Richter, G. Dickeson, A. Astigarraga, T. Tanahashi,

F. Valencia, M. Green, A. Anderson, B. Stridh, A. R. Lagunas Alonso, Y. Sangpongsanont, Guidelines for
Operation and Maintenance of PV Power Plants in Different Climates, Report IEA-PVPS T13-25, ISBN 978-
3-907281-13-0, 2021.

[20]  SolarPowerEurope, “Operation & Maintenance Best Practice Guidelines Version 4.0,” 2019.

[21]  D. H Stamatis, Failure Mode and Effect Analysis: FMEA from Theory to Execution. Quality Press, 2003.

[22]  Guido C. Guerrero-Liquet, Juan Miguel Sánchez-Lozano, María Socorro García-Cascales, María Teresa
Lamata, José Luis Verdegay, Decision-Making for Risk Management in Sustainable Renewable Energy
Facilities A Case Study in the Dominican Republic.

[23]  T. L. Saaty, The Analytic Hierarchy Process; McGraw Hill: New York, NY, USA, 1980.

[24]  M. Mokarram, M. J Mokarram, M. R. Khosravi et al. Determination of the optimal location for constructing

solar photovoltaic farms based on multi-criteria decision system and Dempster–Shafer theory, Sci Rep 10,
8200 (2020). https://doi.org/10.1038/s41598-020-65165-z.

[25]  Life Cycle Assessment (LCA): A Guide to Best Practice | Wiley,” Wiley.com. [Online]. Available:

https://www.wiley.com/en-us/Life+Cycle+Assessment+%28LCA%29%3A+A+Guide+to+Best+Practice-p-
9783527329861. [Accessed: 09-Jun-2021].

44

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

[26]  M. Hauschild, R. K. Rosenbaum, S. Olsen, Life Cycle Assessment: Theory and Practice. Springer

International Publishing, 2018 [Online]. Availa-ble: https://www.springer.com/gp/book/9783319564746.
[Accessed: 09-Jun-2021].

[27]  S. J. Rhee, K. Ishii, Using cost based FMEA to enhance reliability and serviceability, Advanced Engineering
Informatics, vol. 17, no. 3, pp. 179–188, Jul. 2003, doi: 10.1016/j.aei.2004.07.002. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S14740346040.

[28]  F. Dinmohammadi, M. Shafiee, A fuzzy-FMEA risk assessment approach for offshore wind turbines,
International Journal of Prog-nostics and Health Management, vol. 4, no. 13, pp. 59–68, 2013..

[29]  S. Kahrobaee and S. Asgarpoor, Risk-based Failure Mode and Effect Analysis for wind turbines (RB-

FMEA),” in 2011 North American Power Symposium, 2011, pp. 1–7, doi: 10.1109/NAPS.2011.6025116.

[30]  PV Investment Technical Risk Management Best Practice Guidelines for Risk Identification, Assessment

and Mitigation Deliverable D5.8 20/02/2017.

[31]  R. B. Cleveland, W. S. Cleveland, J. E. McRae, and I. Terpenning, "STL: A Seasonal-Trend Decomposition

Procedure Based on Loess," Journal of offcial statistics, vol. 6, no. 1, pp. 3-33, Mar. 1990.

[32]  S. Lindig, I. Kaaya, K. Weiß, D. Moser and M. Topic, "Review of Statistical and Analytical Degrada-tion
Models for Photovoltaic Modules and Systems as Well as Related Improvements,", IEEE Journal of
Photovoltaics, vol. 8, no. 6, pp. 1773-1786, Nov. 2018.

[33]  A. Sayed, M. El-Shimy, M. El-Metwally, M. Elshahed, Reliability, Availability and Maintainability Analysis for

Grid-Connected Solar Photovoltaic Systems, Energies 2019, 12, 1213. https://doi.org/10.3390/en12071213.

[34]  G. Zini, C. Mangeant, J. Merten, Reliability of large-scale grid-connected photovoltaic systems, Renewable

Energy, Volume 36, Issue 9, 2011, Pages 2334-2340, ISSN 0960-1481,
https://doi.org/10.1016/j.renene.2011.01.036.

[35]  W. Herrmann, G. C. Eder, B. Farnung, G. Friesen, M. Köntges, B. Kubicek, O. Kunz, H. Liu, D. Parlevliet, I.
Tsanakas and J. Vedde, Qualification of Photovoltaic (PV) Power Plants using Mobile Test Equipment,
Report IEA-PVPS T13-24: ISBN 978-3-907281-12-3, 2021.

[36]  U. Jahn, M. Herz, M. Köntges, D. Parlevliet, M. Paggi, I. Tsanakas, J. S. Stein, K. A. Berger, S. Ranti, R. H.
French, M. Richter and T. Tanahashi, "Review on Infrared and Electroluminescence Imaging for PV Field
Applications", Report IEA-PVPS T13-10:2018: ISBN 978-3-906042-53-4, 2018.

[37]  K. Sinclair, M. Sinclair, "Silicon solar module visual insepction guide: Catalogue of Defects to be used as a
Screening Tool", https://www.engineeringforchange.org/wp-content/uploads/2017/09/Solar-PV-Product-
Visual-Inspection-Guide.pdf.

[38]  C. Packard, J. Wohlgemuth, S. Kurtz, “Development of a Visual Inspection Data Collection Tool for
Evaluation of Fielded PV Module Condition,” Technical Report NREL/TP-5200-56154 August 2012,
https://www.nrel.gov/docs/fy12osti/56154.pdf.

[39]  G.C. Eder et al., “Error analysis of aged modules with cracked polyamide backsheets,” Solar Energy

Materials & Solar Cells, Vol. 203, December 2019..

[40]  D. Moser et al., “Report on technical risks in PV project development and PV plant operation,”

www.solarbankability.eu.

45

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

[41]  H.E. Yang, R.H. French and L.S. Bruckman, “Durability and Reliability of Polymers and Other Materials in

Photovoltaic Modules,” ISBN 978-0-12-811545-9, 2019..

[42]  T.M. Walsh et al., “Singapore Modules - Optimised PV Modules for the Tropics,” Energy Procedia, Volume

15, page 388-395, 2020..

[43]  K. Petter et al., “Long Term Stability of Solar Modules Made from Compensated SoG-Si or UMG-Si,” Energy

Procedia, Volume 8, page 365-370, 2011..

[44]  All-India survey of photovoltaic module reliability: 2018.

[45]  All-India survey of photovoltaic module reliability: 2013.

[46]  M. Köntges et al., “Mean Degradation rates in PV systems for various kinds of PV module failures,” in Proc.

32nd Eur. Photovolt. Sol. Energy Conf. (EUPVSEC), 2016, pp. 1435 - 1443..

[47]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-

systems/documents/, follow link “Explanation of the PV-System Survey sheet” Version:21 Oc-tober 2019,
last access 04 March 2021.

[48]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-
systems/documents/ follow link to "PV Failure Fact Sheets", last access Aug 2021.

[49]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-

systems/documents/, follow link “Failure survey” Version:21 October 2019, last access 04 March 2021.

[50]  F. Rubel and M. Kottek, “Observed and projected climate shifts 1901-2100 depicted by world maps of the

Köppen-Geiger climate classification,” Meteorol. Zeitschrift, vol. 19, no. 2, pp. 135–141, Apr. 2010,
http://koeppen-geiger.vu-wien.ac.at/shifts.htm, last access 04 March 2021.

[51]  P. Hacke, M.D. Kempe, J.H. Wohlgemuth, J.C. Li, and Y. Shen: Potential-Induced Degradation-

Delamination Mode in Crystalline Silicon Modules, Presented at the 2016 Workshop on Crystalline Silicon
Solar Cells and Modules: Materials and Processes.

[52]  https://iea-pvps.org/research-tasks/performance-operation-and-reliability-of-photovoltaic-

systems/documents/, follow link “Translation tool for geo data to Koeppen_and_Geiger_climate_zone”
Version:21 October 2019, last access 04 March 2021.

[53]  W. Luo et al., “Elucidating potential-induced degradation in bifacial PERC silicon photovoltaic modules,”

Prog. Photovoltaics Res. Appl., vol. 26, no. 10, pp. 859–867, Oct. 2018.

[54]  R. Witteck, M. Siebert, S. Blankemeyer, H. Schulte-Huxel, and M. Kontges, “Three Bypass Diodes

Architecture at the Limit,” IEEE J. Photovoltaics, vol. 10, no. 6, pp. 1828–1838, Nov. 2020.

[55]  G. Oreski, C. Barretta, L. Castillon, P. Christöfl, and M. Köntges, “Importance of bill of material ( BOM )
control and IEC 61215 scope of application,” in 37th European Photovoltaic Solar En-ergy Conference,
2020, p. 4CO.3.1.

[56]  C. Buerhop et al., “PV-Module’s Backsheet Compositions Affecting PV-system’s Yield and Degradation,” in

37th European Photovoltaic Solar Energy Conference and, 2020, pp. 1512–1516.

[57]  DuPont global PV reliability, 2020 Field analysis, Dupont, https://www.dupont.com/news/20200512-2020-

global-pv-reliability-report.html.

46

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

[58]  S. Lindig, “Impact of outdoor effects, degradation and technical failures on uncertainty in energy

performance of photovoltaic systems,” PhD thesis, University Ljubljana, 2021.

[59]  MESIA Solar Outlook Report 2021, accessed: 2021-04-28. [Online]. Available:

https://mesia.com/members/solar-report-2021/.

[60]  "H2020 TRUST PV Project," [Online]. Available: https://trust-pv.eu/. [Accessed 11 01 2021]..

47

Task 13 Performance, Operation and Reliability of Photovoltaic Systems – Quantification of Technical Risks in PV Power Systems

ANNEX 1

48

Component

Module

Defect

Cell cracks

PVFS 1-1vs.01

Appearance  Cell cracks are cracks in the silicon substrate of the photovoltaic cells. Most of the cell cracks
cannot be seen by the naked eye. Only large cracks or where the backsheet is visible through
the  cracks  can  be  seen.  Cell  cracks  can  be  easily  detected through  imaging  techniques like
electroluminescence, UV fluorescence or lock-in thermography. Cell cracks can have different
lengths  and  orientations  (crack  patterns).  Small cell  cracks  (micro-cracks)  become  visible by
eye when they form snail tracks or when photobleaching or delamination takes place along
the cracks. A snail track is a discoloration of the silver paste of the front metallisation of solar
cells which occurs typically 3 months to 1 year after installation of the PV modules. Affected
metal fingers on cells may be silver, yellow or brown in appearance, this effect can also be seen
on cell edges. Photobleaching is a counteracting effect to the yellowing of the encapsulant and
it occurs along the cracks and the borders of the cells. Delamination along cracks is visible as
small bubbles.

Detection

EL, UV (IRT, VI ,IV)

Origin

Impact

Cell cracks can have origin in all lifetime phases of a PV module: production, installation and
operation.  In  production,  cell  cracks can  occur  during wafer,  cell  and module manufacturing.
Especially  the  stringing  and  soldering  process  of  the  solar  cells  can  damage  the  cells.  After
production, major sources for cell cracks are the packaging and transport of the modules, and
the  installation.  After  installation,  external  forces  like  hail,  heavy  snow  weight  or  strong  wind
may result in cell cracks. Once cell cracks are present, further mechanical and thermomechan-
ical stresses can lead to the propagation of the cracks into longer and wider cracks. Some crack
patterns can give indications on the origin of the failure, but the final cause of cell breakage is
not always easy to identify. A repetitive crack pattern can be for example caused by a production
failure, whereas PV modules showing dendritic crack patterns have been probably exposed to
heavy mechanical loads. Snail tracks can be found in a great variety of solar modules, but not
in all. The combination of different materials (encapsulant and back sheets) with UV radiation
and temperature plays an important role in the creation of snail tracks.

Production

Installation

Operation

Cell cracking does not necessarily lead to a failure of the module. The presence of a crack of
any size that does not, or likely will not through its propagation, remove more than 10% of that
cell’s area from the electrical circuit can be considered to have limited to no impact on the per-
formance. Even if each cell in a 60 cell module is cracked, but do not lead to a separated cell
area, the power loss of the module is typically below 2.5 % of the nominal power. In cold and
snow climate zones cell cracks seem to have a more pronounced impact. Here relatively high
mean degradation rates of up to 7%/y can be found. Besides the risk of power loss there is a
risk of hot spots and burn marks due to inactive cell parts. Snail tracks are reported to have
no influence on the performance of the PV module, but due to the observed porous silver fingers
the isolation of cracked cell parts may be accelerated more than it would be without snail tracks.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

transport  proce-
Adequate
dures,  installation  and  clean-
ing  by  trained  personal,  in
case  of  higher  snow  or  hail
risk  use  of  therefore  certified
modules.

Request  EL  pictures  from  pro-
duction, pre-shipment or ware-
house  inspection,  EL  images
with mobile laboratory before or
during  installation,  regular  EL
inspection  or  after
sever
weather conditions.

49

EXAMPLES (page1)

Examples

1-3

PVFS 1-1vs.01

Cell chipping. A very small region
is  missing  from  the  edge  of  the
cell,  but  does  not  enter  metal-
lized region. [16]

Large crack at cell corner visible
by eye - small portion of the cell
(<10%)  is  no  longer  electrically
connected. [16]

Cell crack with snail track. No iso-
lation of  any cell part. The propa-
gation  could  isolate  a  cell  area
>10%.  [16]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

50

Cell cracks visible by the photo-
bleaching effect. This may not be
mistaken for snail tracks. [16]

Two  cell  cracks  with  extensive
delamination, EVA browning and
photo bleaching. [41]

EL  image  of  2  cell  cracks  which
isolates more than 10% of the cell
area. [TUV Rheinland]

Snail track example. [41]

Snail track example. [41]

EL of cell cracks with snail tracks.
[16]

EXAMPLES (page2)

Examples

10-12

PVFS 1-1vs.01

Zoom of snail track with delami-
nation. [41]

Zoom of snail track with browned
fingers. [37]

Zoom of snail track with delamina-
tion. [SUPSI]

Severity

Examples

13-15

Severity

Examples

16

Severity

Cell  crack  with  EVA  delamina-
tion.  [TUV  Rheinland]  (see  also
PVFS 1-3)

Typical EL picture of a cell crack
caused by hail. [TUV Rheinland]

Repetitive crack pattern due to im-
soldering  machine.
pact
[SUPSI]

of

Typical EL picture of cell cracks caused by a heavy homogeneous
mechanical load (X-crack pattern) also without glass breakage. [16]

51

Component

Module

Defect

Discolouration of encapsulant or backsheet

PVFS 1-2vs.01

Appearance  The degradation of the encapsulation or backsheet materials is getting visible as a light yellow
to dark brown discolouration.  Colour can be next to or above the cells, along the busbars or
cell interconnects or on the back or front side of the backsheet. Often discolouration is inho-
mogeneous and follows spatial patterns depending on the type of module construction. Typi-
cally, for glass/backsheet modules the browning occurs in the central region of the cells with
wide clear encapsulant areas, or “frames” around the cell edges. Discolouration can also be
observed in the encapsulant between neighbouring solar cells when the front side of the back-
sheet (layer behind the cells) is degrading. For glass/glass module constructions the encap-
sulant discolouration is mostly spatially uniform, but can also show patterns of clearer areas
over some cells. In glass/backsheet modules the location of these patterns generally corre-
lates with cell cracks. In some cases, the discolouration is more pronounced in one or more
cells of the module.

Detection

VI, (IV, IRT)

Origin

Impact

In the past, yellowing or browning was mostly associated with the degradation of the mostly
used  encapsulant  ethylene  vinyl  acetate  (EVA)  but  this  problem  was  greatly  solved  by  im-
proved stabilisation of the polymer with additives, including UV absorbers and thermal stabi-
lizers. If the choice of additives and/or their concentrations are inadequate, or the lamination
process is inadequate or incomplete, the encapsulation material may discolour over time. The
patterns of discolouration observed in the field can be very complex because of the diffusion
of oxygen or the products of reaction, such as acetic acid, generated when heat and UV light
interact with EVA. The presence of oxygen leads to the so called photobleaching effect which
creates a ring of transparent EVA around the perimeter of a cell or a cell crack. The case of
single cells which are far darker than the adjacent cells, implies that the most discoloured cell
was at higher temperature than the surrounding cells, perhaps because of differences between
the cells or the cell being located above the junction box.

Production

Installation

Operation

Discoloration is a sign that the polymeric compounds within the module started to degrade.
This type of degradation is predominantly considered to be first an aesthetic issue before a
decrease of module current and power production is detected. Typically, mean yearly degra-
dation rates due to yellowing are about 0.5%/a and may reach up to 1%/a in hot and humid or
moderate climates. While it is uncommon for EVA discolouration to induce other failures within
the cell, it may correlate to: high temperatures in the field, the generation of acetic acid and
concomitant corrosion and embrittlement. Unless discolouration is very severe and localized
at a single cell, where it could cause a substring bypass-diode to turn on, the discolouration of
EVA does not present any direct safety issues. More critical is the discolouration of UV sensi-
tive  backsheets  that  can  result  in  a  loss  of  mechanical  properties  (elastic  behaviour)  and
cracking of backsheet due to thermomechanical stresses.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Check  validity  of  IEC  61215
certification and BOM.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

Regular system inspections

For areas with harsh climate,
request  modules  pass  higher
test  standards,  like double or
triple  IEC  61215  test  condi-
tion.

52

EXAMPLES (page1)

Examples

1-3

PVFS 1-2vs.01

Slightly browned EVA in the cen-
tre of the cell with photobleaching
at the edges. [16]

Slightly browned EVA in the cen-
tre of the cell with photobleaching
at the edges. [44]

Yellowed backsheet from the in-
side. [37]

Severity

Examples

4-6

Severity

Examples

7

Dark discolouration at cell edges,
between cells and over gridlines
and busbars. [37]

Dark  discolouration  over  metali-
zation. [37]

Backsheet  air  side  yellowing.
[37]

Single cell browned much faster
than the others due to local heat-
ing. [16]

Severity

53

Component

Module

Defect

Front delamination

PVFS 1-3vs.01

Appearance  Any local separation of the layers between (i) the front glass and the encapsulant or (ii) the
cell and the encapsulant, visible as bubbles or as bright, milky area/s. It may appear continu-
ous or in spots. The position and size of the delamination or bubble depends on the origin and
progress of the failure.

Detection

VI, (INS)

Origin

Impact

The adhesion between the glass, encapsulant, active layers, and back layers can be compro-
mised for many reasons. Typically, it is caused by the manufacturing process (e.g. poor cross
linking of EVA, too short lamination times, too high pressure in the laminator, contaminations,
improper cleaning of the glass, incompatibility of EVA with soldering flux, inadequate storage
of  the  raw  material)  or  environmental  factors  (e.g.  thermal  stresses,  external  mechanical
stresses,  UV).   Delamination  is  generally followed  by  moisture  ingress and  corrosion. It  is
therefore more frequent and severe under hot and humid conditions.

Production

Installation

Operation

Delamination or bubbles do not automatically pose a safety issue, but they can result in re-
duced insulation of the component and increased safety risk when they form a continuous
path between electric circuit and the edge due to possible water ingress. Moisture in the mod-
ule will decrease performance due to an increase of series resistance, affect long term relia-
bility and in some cases also the structural integrity of the module. Moreover, delamination at
interfaces in the optical path will result in additional optical reflection and subsequent decrease
in  current.  This  can  be  the  origin  of  current  mismatch.  If  the  mismatch  is  significant,  it  will
trigger the bypass diode and cause further power loss. The inverter might also shut down due
to leakage current’s leading to a further performance loss. Manufacturing related delamination
issues often affects a relevant percentage of modules within the same production batch and
consequentially has a big impact on system performance.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Check  validity  of  IEC  61215
certification and BOM, ground
fault  detection  by  inverter  or
other devices at all time.

Extended  testing  (e.g.  damp
heat),  pre-shipment  inspec-
tions  (e.g.  cross  linking  level
of EVA) regular visual system
inspections.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules. In case of in-
dividual  module
testing  all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.

54

EXAMPLES (page1)

Examples

1-3

PVFS 1-3vs.01

Encapsulant delamination in un-
critical position. [SUPSI]

Encapsulant  delamination  from
cell  caused  by  production  pro-
cess. [SUPSI]

Encapsulant  delamination  from
cell  along  grid  fingers  and  bus
bar. [38]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

Encapsulant  delamination  from
glass  (spotted  due  to  glass  tex-
ture) along the bus bars. [37]

Encapsulant delamination along
a cell crack. [46] (see also PVFS
1-1)

Encapsulant  delamination  near
cell edges in combination with cell
browning. [38]

Delamination in front of cell in the
centre  of  the  module.  [40]  (see
also FS 1-2)

Delamination  at  module  insert
connections  of  a  glass/glass
module (junction box). [SUPSI]

Delamination at cell edges. [16]

55

EXAMPLES (page2)

Examples

10-12

PVFS 1-3vs.01

Encapsulant delamination at bor-
ders. [37]

Encapsulant delamination along
a  bus-bar  in  a  cell  close  to  the
module edge. [40]

Encapsulant delamination of from
glass  (spotted  due  to  glass  tex-
ture) at the edge of the cell. [37]

Delamination creating a continu-
ous path between electric circuit
and the edge. [40]

Delamination  with  corrosion.  [1]
(see also FS1-11)

Delamination  caused  by  detach-
ment of backsheet with exposure
of  encapsulant  from  the  back.
[SUPSI]

Severity

Examples

13-15

Severity

56

Component

Module

Defect

Backsheet delamination

PVFS 1-4vs.01

Appearance  Any  local  separation  of  the  polymeric  back  sheet  layers  leading  to  an  air  gap  between the
backsheet and the rest of the module, or within the multilayer backsheet (=internal delamina-
tion). The backsheet may appear wavy, with locally limited bumps, bubbles or ripples. In the
worst case, one or more layers may peel off. The position and extent of the delamination will
depend on the cause and progression of the failure.

Detection

VI, (INS)

Origin

Impact

There are many different forms and compositions of polymeric multilayer backsheets on the
market. With laminated backsheets (polymeric layers adhered to each other by a thin adhesive
layer)  internal  delamination  can  appear:  the multiple  layers may delaminate  upon  adhesive
degradation, which may lead to local delamination of two subsequent layers or a peel-off of
one or more layers. Co-extruded backsheet are prone to internal lamination. Delamination of
the backsheet from the encapsulant can appear with all types of backsheets and originates
from a lack of adhesion between the backsheet and the encapsulation. The major drivers for
the delamination of or within the the backsheet are (i) thermo-mechanical stress originating
from differing CTE of the individual polymeric layers, (ii) chemical reactions at the interfaces
(material incompatibility) or deteriorated interfacial bonding as a result of the attack from heat,
UV and moisture or (iii) external mechanical stress applied on the module. Therefore, it is more
frequent and severe under hot and humid conditions. Delamination can be also caused by an
insufficient lamination process e.g. too short lamination times.

Production

Installation

Operation

If delamination occurs forming bubbles in a central, open area of the back, it will not present
an immediate safety issue. That area would likely operate at slightly higher temperatures as
the heat conduction/dissipation through the backsheet is disturbed. But as long as the bubble
is not further mechanically cracked or expanded, the performance and safety concerns are
minimal. However, if delamination of the backsheet occurs near a junction box, or near the
edge of a module there would be more serious safety concerns. Delamination at the edge may
provide a direct pathway for liquid water to enter the module during a rainstorm, or in response
to the presence of dew. That can provide a direct electrical pathway to ground creating a very
serious safety concern. Similarly, delamination near a junction box can cause its loosening,
putting  mechanical  stress  on  live  components  with  the  danger  of  breakage.  A  break  might
cause a connection failure to a bypass diode and possibly result in an unmitigated arc at full
system voltage. In multilayer backsheets the severity depends also on which layer is affected.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Regular system inspections.

Check  validity  of  IEC  61215
certification and BOM.

Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules. In case of in-
dividual  module
testing  all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.

57

EXAMPLES (page1)

Examples

1-3

PVFS 1-4vs.01

Multiple  bubbles  in  the  centre
and edge of the backsheet. [46]

Blisters  because  of  vapour  bar-
rier, such as aluminium foil. [1]

Big central bubble + wavy delam-
ination. [16]

Backsheet  delamination  with  di-
rect  exposure  of  encapsulant.
[SUPSI]

Delamination of top layer without
exposure
encapsulant.
[SUPSI]

of

Severity

Examples

4-5

Severity

58

Component

Module

Defect

Backsheet cracking

PVFS 1-5vs.01

Appearance  Any damage of the backsheet (surface or whole stack) that is visible as crack, burst or scratch.
The location and extent of the cracks depend on the cause and progression of the failure. The
cracked  area may  be  localized  (e.g bursted  bubble,  scratch),  extend  along  specific module
areas (e.g. long or between the cells, along the busbars) or extend over large or the full area
of the module (e.g embrittled surface). The crack can be very deep and affect the back sheet
stack.

Detection

VI, (INS)

Origin

The degradation of the backsheet can be caused by environmental factors like UV-irradiation,
thermal stress, external mechanical stress or by internal stress (e.g. thermomechanical stress
with the multimaterial composite PV-module) or incorrect handling during transport and instal-
lation (local cuts, scratches). Deep backsheet cracking (whole backsheet stack split) is often
followed by moisture ingress and corrosion. This is more frequent and severe under hot and
humid  conditions.  The  use  of  low  quality  material  (e.g.  low  UV  resistance)  or  incompatible
material combinations (backsheet ↔ encapsulant) causes most of the premature degradation
failures. Discolouration and or strong chalking can be precursors for backsheet cracking.
Deep cracks or bursted bubbles can be the result of  local hotspots/burn marks that split or
break the backsheet.

Production

Installation

Operation

Impact

A  broken  backsheet  can  cause  electrical  insulation  failure,  posing  a  safety  hazard  and  a
potential ground fault. On the long-term, power degradation due to the penetration of moisture
into the module which induces further failures (e.g. corrosion, delamination) can occur. In the
case of deep cracks reaching the active part of the cells, the insulation is immediately com-
promised and safety is not anymore fulfilled.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Regular system inspections.

Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time,  check  validity  of  IEC
61215 certification  and BOM,
visual  inspection  before  in-
stallation.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules. In case of in-
testing  all
dividual  module
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.

59

EXAMPLES (page1)

Examples

1-3

PVFS 1-5vs.01

Cracked  backsheet  in  combina-
tion  with  yellowing  under  a  hot
cell. [39]

Squared  cracks  beneath  cell  in-
terspaces. [39]

Cracking between cells. [38]

Severity

Examples

4-6

Severity

Examples

7-8

Severity

60

Longitudinal cracks located under
bus bars. [39]

Backsheet cracking. [57]

Backsheet cracking. [57]

Localized superficial damage. [1]  Deep scratch on backsheet. [TUV

Rheinland]

Component

Module

Defect

Backsheet chalking (whitening)

PVFS 1-6vs.01

Appearance  White powder is detectable on the external surface of the backsheet. It can be seen by passing
a finger over the backsheet. It can be removed. The backsheet has usually a rough or dull
appearance.

Detection

VI

Origin

Impact

Chalking is caused by the photothermal degradation of the polymers in the outer backsheet
layer containing inorganic pigments. For example, TiO2 pigments are often used in the outer
layers as UV blocker.

Production

Installation

Operation

Chalking does not affect module safety or performance on first sight, but it can be a sign for
an ongoing degradation of the backsheet and a precursor for severe backsheet cracking. Due
to the degradation-induced reduction of UV protection, more serious failures, such as back-
sheet cracking and insulation failures can occur. Enhanced moisture diffusion into the en-
capsulant/active PV-parts can lead to corrosion of cells and connectors, having a negative
impact also on the performance.

Safety:

Performance:

Mitigation

Corrective actions

inspections  should
Regular
be  done  to  monitor  the  pro-
gress of the observed failure.
Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time.

Preventive actions
 (recommended)

Preventive actions
(optional)

Check  validity  of  IEC  61215
certification and BOM.

Regular system inspections.

61

EXAMPLES (page1)

Examples

1-2

PVFS 1-6vs.01

Finger  with  white  powder.  [TUV
Rheinland]

Fingerprint  on  a  module  with
chalking. [TUV Rheinland]

Severity

62

Component

Module

Defect

Burn marks

PVFS 1-7vs.01

Appearance  Burn marks are visible with the naked eye as burnt, blackened area/s. The burn mark may
lead to bubbling or melting of the polymeric encapsulant, and/or glass breakage or a hole in
the backsheet.  Burn marks on the backheet may be not visible from the front requiring an
inspection with an IR camera if the back of the module is not accessible. They may however
not be visible by IR inspection in case no further or ongoing heating occurs.

Detection

VI, IRT, (EL)

Origin

Impact

The defect is associated with parts of the module that became very hot because of production
errors (e.g weak solder bonds, ribbon breakage, incomplete cell edge isolation, alignment er-
rors,  metal  particles)  and/or  transportation/handling  errors  (e.g,  cracked  cells,  damaged
back-sheet) in combination with one or more operational factors (e.g. shadowing, open cir-
cuited bypass diodes, reverse current flows).  Physical stress during PV module transporta-
tion,  heavy  snow  loads,  a  lightning  strike,  thermal  cycling,  and/or  hot  spots  by  partial  cell
shading during long-term PV system operation forces mechanical weak(ended) cell/connec-
tion parts to break. Burn marks occur for example when a reverse current flow causes heating
that further localizes the current flow, leading to a thermal runaway effect and the associated
burn mark.

Production

Installation

Operation

Burn marks on interconnections are often associated with power loss, but if redundant electri-
cal interconnections are provided, a failed solder bond may have negligible effect on the power
output. If all solder bonds for one cell break, then the current flow in that string is completely
blocked and an electric arc can result if the current cannot be bypassed by the bypass diode
and the system operates at high voltage. Performance, reliability and safety are likely to be
severely compromised. Such an arc can cause a fire if there happen to be flammable material
around. If there is a question about whether the existence of the burn mark requires replace-
ment of the module, an infrared image under illuminated and/or partially shaded conditions will
quickly  identify  whether  the  area  is  continuing  to  be  hot  and/or  whether  current  flow  has
stopped in that part of the circuit. Temperature difference between neighbouring cells should
not be over 30 K. At this stage safety risk may still be not so high because the temperature of
this hot spot cell does not increase to more than around 100 °C. Also edge isolation faults
on the solar cell level are under normal conditions not problematic, but when the bypass diode
is in open-circuit, the current is driven in reverse through the shunts of the solar cells and burns
the encapsulation.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

Visual  inspection  before  in-
stallation,  commissioning  of
system with IRT.

Regular system inspections.

63

EXAMPLES (page1)

Examples

1-3

PVFS 1-7vs.01

Burn mark at the backsheet with
cracked backsheet. [37]

Burn marks at the backsheet due
to heating along a busbar. [16]

Burn mark associated with over-
heating along the metallic inter-
connection  (without  backsheet
damage). [16]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

64

Front and back side view of burn marks caused by open-circuited by-
pass  diodes  and  current  mismatch  conditions  (due  to  shading  or
cracked cells). [16]

Burn  marks  caused  by  defect
bypass  diodes  or  an  intercon-
nect failure in the junc. box. [16]

Burn  mark  with  broken  glass
caused  by  poor  bussing  ribbon
soldering. [41] (s. also PVFS 1-8
and PVFS 1-8)

Burn mark due to intrinsic shunt-
ing  caused  by  error  in  manufac-
turing process. [41]

intrinsic
Burn  mark  due
shunting  caused  by  error  in
manufacturing process. [41]

to

Component

Module

Defect

Glass breakage

PVFS 1-8vs.01

Appearance  Glass is cracked locally or over the full area of the module. Glass breakage looks different
depending on the type of glass and the origin of the glass breakage. Tempered glass or heat-
treated  float  glass  will  shatter  into  small  pieces,  whereas  annealed  glass  breaks  into  big
pieces. Heat-treated glass stays in between.

Detection

VI, IRT

Origin

Impact

Glass breakages of the front glass can be caused by heavy impacts such as hail or stones or
other  extreme  mechanical  stress  onto  the  module  frame  due  to  external  stresses  or  bad
mounting.  High  temperatures  (hot-spot  or  arc)  can  also  break  the  glass.  Annealed  glass
breaks also due thermal gradients or stress induced by the lamination process or cleaning of
the  modules.  A  relatively  often  seen  failure  in  the  field  is  glass  breakage  of  frameless  PV
modules caused by the clamps. Glass/glass modules are more sensitive to glass breakage.
The origin of the failure is, on the one hand, at the planning and installation stage either (a)
poor clamp geometry for the module, e.g. sharp edges, (b) too short and too narrow clamps
or (c) the positions, kind or number of the clamps on the module not being chosen in accord-
ance with the manufacturer’s manual. The second origin which induces glass breakage could
be excessively-tightened screws during the mounting phase or badly-positioned clamps. The
glass  of  some  PV  modules  may  also  break  due  to  vibrations  and  shocks  occurring  during
transportation or handling. Another reason for glass breakage comes from impact stresses on
the glass edge. Sometimes vandalism or animal damage happens, the animals like goats like
to climb on the PV modules, and birds may drop stone or other objects from the sky.

Production

Installation

Operation

Module mechanical integrity is compromised when the glass is broken. Over time glass break-
age  leads  to  loss  of  performance  due  to  cell  and  electrical  circuit  corrosion  caused  by  the
penetration  of  oxygen  and  water  vapour  into  the  PV  module.  Shattering  of  tempered  glass
usually also breaks the cells reducing the power of the module and increasing the risk of hot
spots. Mechanical and electrical safety is thus compromised. Firstly, the insulation of the mod-
ules is no longer guaranteed, in particular in wet conditions. Secondly, glass breakage causes
hot spots, which lead to overheating of the module. A module with a completely broken glass
lead to current and power reductions in the whole string.

Safety:

  Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

All  damaged  modules have
to be replaced.

transport  proce-
Adequate
dures,  installation  and  clean-
ing  by  trained  personal,  in
case  of  higher  snow  or  hail
loads  use  of  certified  mod-
ules.

Regular system inspections.

65

EXAMPLES (page1)

Examples

1-3

PVFS 1-8vs.01

Chipped glass at the corner. [38]  Glass  breakage  along  the  string
interconnect ribbons due to weak
manufacturing process. [SUPSI]

tempered
Glass  breakage  of
glass  induced  by  a  hot-spot.
[SUPSI]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

66

Glass  breakage  caused  by  too
tight screws. [16] (see also PVFS
3-1)

Glass  breakage  caused  due  to
poor clamp design. [16]

Glass  breakage  caused  due  to
poor clamp design. [1] (see also
PVFS 3-1)

Glass  breakage
through  high
temperature  gradient  and  not
tempered glass. [16]

Glass  breakage  of
tempered
glass  induced  by  burn  mark.  [1]
(see also PVFS 1-7 and PVFS 1-
9)

Breakage of tempered glass. [1]

EXAMPLES (page2)

Examples

10-12

PVFS 1-8vs.01

Direct lightning stroke. [46]

Impact  damage  caused  by  a
heavy object. [SUPSI]

Hail damage. [SUPSI]

Severity

67

Component

Module

Defect

Cell interconnection failure

PVFS 1-9vs.01

Appearance  Weak or broken cell or string interconnection are not easy to see by the naked eye. The failure
can be identified as dark region in the electroluminescence image where the failed intercon-
nect would otherwise be collecting carriers or as a hot spot in the infrared image. In a pro-
gressed stage burn marks and glass breakage can occur.

Detection

EL, IRT, STM, (VI)

Origin

Impact

Typically,  it  is  caused  by  the  manufacturing  process  (e.g.  poor  soldering,  misplacement  of
ribbons, too  intense  deformation  of  the ribbon  kink,  narrow  distance between the  cells) fol-
lowed  by thermomechanical  stress  or  repetitive wind  load  caused  by the  outdoor  operating
environment. Electrochemical corrosion can be another cause for the degradation of inter-
connections.

Production

Installation

Operation

Poor  interconnections  (soldering  bonds)  lead  to  an  increase  of  contact  resistance,  higher
power dissipation and localized heating. Broken connections are often associated with power
loss, but if redundant electrical interconnections are available, a failed connection may have
negligible effect on the power output. Safety risk may be not so high until the temperature of
the induced hot spot does not increase to more than around 100 °C. If all busbars of a cell
are interrupted, then the current flow in that string is completely blocked and an electric arc
can result if the current is not bypassed by the bypass diode and the system operates at high
voltage. The safety risk depends on the durability of this bypass diode. A bypass diode, which
is continuously active over days can be damaged and pass into open-circuit or short circuit
state. As a result of an open circuited diode, the current goes through the failed cell string
and generates heat at the disconnected position. Very high temperatures or an electric arc
and may cause fire, open electrical conducting parts to the user and destroy the mechanical
integrity of the module.

Safety:

  Performance:

Mitigation

Corrective actions

Preventive  actions  (recom-
mended)

Preventive actions              (op-
tional)

Check  validity  of  IEC  61215
certification and BOM.

Regular system inspections.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

68

EXAMPLES (page1)

Examples

1-3

PVFS 1-9vs.01

Zoom  of  a  broken  cell  intercon-
nect. [41]

EL image of a module with 3 cells
with  disconnected  interconnect
ribbons. [16]

Disconnected  cell  interconnect
with delamination. [1]

Severity

Examples

4-6

Severity

Dislocation  of
ribbon. [37]

interconnection

Poor  soldering  of  string  inter-
connect leading to burn mark and
broken  glass.
[41]  (see  also
PVFS 1-7 and PVFS 1-8)

Mirco arc which occur if the con-
ductive  glue  on  the  string  inter-
connect  has  an  insufficient  con-
tact. [16]

69

Component

Module

Defect

Potential induced degradation (PID) (page1)

PVFS 1-10vs.01

Appearance  A potential induced degradation (PID) is not directly visible by eye. It is recognisable as an
overtime increasing power loss, which is easily observable only a few years after installation.
Infrared thermography (IRT) imaging of operational PV modules in the direct sunlight  is the
most  straightforward  method  for  getting  the  evidence  of  PID  degradation.  Typical  PID  IRT
patterns (warmer cells close to the bottom frame or patchwork patterns) and PV modules po-
sitioned close to one of the poles of the module string are strong indications for PID. The most
efficient,  but  more  complex  and  expensive  detection  method  for  PID  is  to  take  EL  images.
When taken at 1/10 of the rated current it can detect PID also in an early stage, before a power
loss can be noticed. It’s because in the early stage, the PID degradation is more pronounced
at low light conditions. To quantify the performance loss, I-V measurements have to be per-
formed on the affected string and/or modules. In an advanced stage secondary induced fail-
ures like hot-spot’s, yellowing and/or corrosion can be sometimes observed.

Detection

IV, EL, IRT, (MON)

PID  is  a  degradation  mode  induced  by  a  high  voltage  stress  with  respect  to  ground.    The
occurrence of this failure depends on the magnitude of the voltage (number  of serially con-
nected  PV  modules  per  string)  and  the  polarity  of  the  electrical  field  build-up  between  the
framing/glass surface and the solar cells. The last depends on the inverter typology (trans-
former), the grounding concept and cell technology. Modules with p-type cells degrade in neg-
ative polarity strings whereas modules with n-type cells in strings with positive polarity. PID
degradation is more pronounced the higher the potential to which a single cell within a module
or string is subjected. The PID effect is therefore stronger in cells that are located at the edges
of the module (close to frame) and to the bottom of a string with an increase towards one end
of the string. The degradation is further accelerated by temperature, humidity, rain (surface
wetting), condensation and soiling. Two different types of PID are known for crystalline silicon
modules: PID-p (polarization) and PID-s (shunting). The PID-p was observed for the first time
in back contact cells within Sunpower modules. PID-p is caused by the build-up of negative
surface charges on the cells, which results in a current loss. The PID-s is induced by leakage
currents through the module’s front glass and the encapsulation material. The flow of Na+ ions
mainly from the glass into the cell leads to the creations of shunts.  For both PID types, module
and cell design has a fundamental influence if and how much a module is affected by PID.
There are modules on the market which are designed to be PID resistant.

Production

Installation

Operation

Yield losses of 20 percent and more within 1 year were observed in the past. The PID-s effect
causes a reduction of I-V curve fill factor and output power. Short circuit is affected only in a
very progressed state. Due to its catastrophic performance loss PID-s bears a high economic
risk.  PID-s is to some extent a reversible polarization effect and can therefore ‘repaired’ or
omitted when detected in time. If detected too late the PV system can’t be repaired and non-
reversible damages has to be taken into account.  The PID-p effect causes instead a signifi-
cant reduction of short circuit current, open circuit voltage and power. PID-p can be fully re-
generated by reversing the polarity of the bias potential. Up to now safety problems directly
related  to  the  PID  are  not  reported,  but  hot  spots  and  corrosion  caused  by  the  strong  cell
mismatch may cause later safety issues. The PID sensitivity of PV modules can be tested in
the laboratory. Anti-PID insurance can be obtained, although many insurers need to be edu-
cated about the phenomenon for correct risk estimation and pricing.

Safety:

Performance:

Origin

Impact

70

Component

Module

Defect

Potential induced degradation (PID) (page2)

PVFS 1-10vs.01

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Modules  tested  for  PID  ac-
cord.  IEC  62804-1  should  be
less  prone  to  PID  (verify  that
BOM corresponds!)

PID  prevention  at  system
level: The installation of an in-
verter with transformer can be
considered
as  mitigation
measure for the PID phenom-
enon. On the other hand, the
trade-off with the inverter effi-
ciency and the cost of the in-
verter  must  be taken into ac-
count. Anti-PID insurance.

How to proceed depends very
much  on  the  stage  on  which
PID is detected. If detected in
an  early  stage  recovery  is
possible by applying a reverse
voltage  during  night-time.
Specific anti PID kits are avail-
able on the market promising
a  recovery  of  the  lost  power.
As there is not a full guarantee
that the recovery will be effec-
tive for the specific situation, it
should be monitored or meas-
ured to see if the problem has
been sufficiently solved. In the
case of progressed PID with-
out  visible  module  damages,
the recovery could need sev-
eral  months  or  even  years
suggesting  in  any  case  a  re-
placement of all modules with
modules tested to be PID re-
sistant.

71

EXAMPLES (page1)

Examples

1-2

PVFS 1-10vs.01

Strings with PID, detected with IR thermography. [16]

Dark IR thermography at Isc for a module
affected by PID. [16]

Severity

Examples

3-4

Severity

Examples

5-6

Strings with PID, detected with EL imaging.

Electroluminescence  image  made  at  Isc
for a module affected by PID. [16]

2.

1.

3.  PID affected module with power loss of 89%, left: EL at 1.5

x Isc, right: I-V curve of the same module at 1000 and 200
W/m2. [35]

PID  affected  module  with  power  loss  of
14%. top: EL at 1.5 x Isc. bottom: EL of the
same module at 0.2 x Isc.  [35]

Severity

72

Component

Module

Defect

Metallisation discolouration/corrosion

PVFS 1-11vs.01

Appearance  The discolouration and/or corrosion of the cell metallisation and the interconnections is getting
visible as a light yellow to dark brown to black discolouration of the electrical parts. Depending
on the material combinations corrosion is furthermore noticeable by the presence of galvanic
products  that  may  appear  powdery,  white,  light  gray,  and/or  have  a  yellow,  blue,  or  green
tinge.  The  defect  occurs  typically  at  the  solder  bonds,  on  the  cell  gridlines/fingers  or  the
cell/string interconnect ribbons. It is very often observed together with other failures like de-
lamination and discolouration of the encapsulant and sometimes with burn marks.  Under
certain circumstances corrosion is more visible near cell edges. Dark areas at the cell borders
of the EL images can here highlight the diffusion of moisture through the rear side of the mod-
ule and the gaps between the cells and the subsequent front side cell corrosion starting from
the edges.

Detection

VI, (EL, IV)

Origin

The corrosion/oxidation of the metallisation is caused by the presence of moisture and acidity
in the encapsulant, as e.g. acetic acid, a degradation product of the mostly used encapsulant
EVA or remaining crosslinker (peroxides). Acetic acid has a corrosive effect on the cell metal-
lisation and the cell interconnect. The ingress of moisture caused by an ongoing delamination
process leads together with the oxygen to a further acceleration of the corrosion. Corrosion
can be caused by a poor manufacturing process (e.g residual crosslinker due to a too short
lamination process; imperfections in cell soldering) or the choice of poor materials (low corro-
sion resistance of tin-based coating of copper ribbons, high water permeability of back sheet
and/or encapsulant materials). Environmental factors can  accelerate the corrosion (e.g am-
monia, salt, humidity, temperature).  For these reasons, corrosion is more frequent and severe
under hot and humid climates or in agriculture or maritime environments. Discolouration can
be also related to non-corrosive processes like a discolouration due to light-sensitive solder
flux residues on the ribbon.

Production

Installation

Operation

Impact

The metallisation, and/or interconnect, corrosion leads to an increased series resistance and
therefore losses in module performance. The power loss is less pronounced for modules with
metallisation discolouration without corrosion. The defect does not automatically pose a safety
issue. Locally increased series resistance leads to current mismatch. If the mismatch is getting
significant, it can trigger the bypass diode and cause further power loss of the PV module.

Safety:

Performance:

Mitigation

Corrective action

Preventive actions
(recommended)

Preventive actions
(optional)

Check  validity  of  IEC  61215
certification and BOM.

Regular system inspections.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

73

EXAMPLES (page1)

Examples

1-3

PVFS 1-11vs.01

Discolouration  due  to  corrosion
or to light-sensitive flux residues
on the ribbon.

Discolouration due to corrosion
on the ribbon. [SUPSI]

String interconnect corrosion. [1]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

74

Cell interconnect corrosion. [1]   Modules with light Ag finger oxi-

dation after 5 years in the field.

[41]

Severe  oxidation/corrosion  and
burn  marks  on  the  Ag  fingers,
interconnects
busbars,
of modules after 25 years. [41]

and

Corrosion  seen  as  red,  green
and  black  discolouration  in  the
string interconnect. [41]

Busbar  corrosion  and  delamina-
tion at the edge. [SUPSI]

Glass/glass module showing de-
lamination  and  subsequent  cor-
rosion. [1]

Component

Module

Defect

Glass corrosion or abrasion

PVFS 1-12vs.01

Appearance  The degradation of the glass front layer is getting visible as a homogenous or heterogeneous
change  in  colour and  transparency  of  the  glass.  The affected  glass  surface  can  appear  hazy  or
milky and in some cases also rougher compared to the non-degraded module/module area.
Increased susceptibility to soling could be observed.

Detection

VI, (IV)

Origin

To optimise the efficiency and appearance of a PV module most manufacturers apply some
anti-reflective coatings (ARC), anti-soiling coatings (ASC) or multilayer coatings on the front
of their modules. 1-3% more power can be obtained by these techniques respect to module
with uncoated glass. Corrosion or abrasion of these layers can however, reduce or vanish the
effectiveness of these coatings. Glass corrosion is caused by atmospheric humidity in combi-
nation with gases or particles present in the atmosphere (e.g. pollutants, salt, ammonia) and
the glass. It happens for example when water (dew) dissolves some of the sodium ions from
the top of the soda lime glass, leading to the production of an alkali base that can then corrode
the glass silicate. Glass abrasion or corrosion can be also caused by inappropriate cleaning
techniques (mechanical removal techniques, inappropriate cleaning agents) which damage or
removes the coatings. Abrasion occurs mostly in the desert, due to the combination of wind,
sand and dust which causes abrasion and frosting of the glass surface.

UV or voltage induced degradation effects can further accelerate the degradation of the coat-
ings.

Production

Installation

Operation

Impact

Corrosion or abrasion of the glass front layer lowers the transmission of the glass, leading to
a power loss. The power loss is generally limited to a few percent and is saturating over time
except in the case where the soiling susceptibility is significantly increased and larger losses
can be observed. Operating and Maintenance (O&M) costs can be affected by this.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Regular system inspections.

Check  validity  of  IEC  61215
certification and BOM, appro-
priate component selection in
function  of  intended  applica-
tion.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Depends on the
level of performance loss. For
extreme  environments  (e.g.
near  to  mines,  cement  facto-
ries),  evaluate  cost-effective-
ness  of  replacing  modules
with lost yield.

75

EXAMPLES (page1)

Examples

1-3

PVFS 1-12vs.01

Zoom of module with hazy glass
(homogenous  discoloration)  due
to surface corrosion. [45]

Zoom of module with hazy glass
(heterogenous discoloration) due
to surface corrosion. [43]

Hazy  glass  due  to  glass  corro-
sion close to frame. [44]

Glass corrosion on the front of a mono-Si back-contact module after
damp heat 90/90 testing. [42]

Glass corrosion. [46]

Severity

Examples

4-5

Severity

76

Component

Module

Defect

Defect or detached junction box

PVFS 1-13vs.01

Appearance  The junction box housing and lid appears either defect (weathered, brittle, cracked, warped,
melted or burned) and/or detached (open or loose lid, shifted or detached junction box from
backsheet). The sealant/adhesive material with which the junction box is attached to the back-
sheet can be weathered or appear as yellowed.  The sealing components/material around the
wire entrance or the lid can be damaged (squeezed, broken, brittle) or completely missing.

Detection

VI

Origin

Junction box detachment results from poor fixing of the junction box to the backsheet or use
of low quality adhesive. Acrylic or PE Foam tapes were used as junction box attachment ma-
terial in early years, but they frequently loss stickiness at low temperature and result in de-
tachment.  Use of inadequate IP rating junction box may cause water intrusion and subsequent
failure.  Opened or badly closed j-boxes may due to poor manufacturing process or air pres-
sure caused by high temperature for boxes with no exhaust path. Delamination near a junction
box can cause it to become loose. Improper handling or mounting of the modules can be also
the cause of damages the j-box, like pulling modules up on the cables before mounting, or
missing cable fixing or usage of too short cabling to interconnect modules to a string, causing
frequent or permanent mechanical stress on the j-boxes.

Production

Installation

Operation

Impact

A defect or detached junction box is causing humidity ingress with corrosion of the intercon-
nections, leading to performance losses and increasing risk of electrical arcing and subse-
quent initiation of fire. Furthermore, a loose junction box is putting mechanical stress on the
contacts within the junction box, with the risk of breaking them and exposing persons to active
electrical components.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Modules with a direct safety
risk or a severity of 5 should
be  replaced  or  repaired.
Regular
inspections  should
be done to monitor the status
of the not replaced modules.

Check  validity  of  IEC  61215
certification and BOM.

Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time.

Regular system inspections.

77

EXAMPLES (page1)

Examples

1-3

PVFS 1-13vs.01

Poorly  bonded  junction  box  on
the backsheet. [16]

Open  junction  box  in  the  field.
[41]

Detached
backsheet. [SUPSI]

junction  box

from

Severity

Examples

4-5

Severity

Examples

6-7

Severity

78

Left:  Missing  junction  box  lid  sealing  with  corrosion  of  contacts.
Right: Good junction box sealing.   [45]

Missing  seal  or  strain  relive  of
module  cables,  improper  cable
inlet. [37]

Melted junction box. [TUV Rhein-
land]

Burned  junction  box  caused  by
corroded  contacts  within
the
junction box. [TUV Rheinland]

Component

Module

Defect

Junction box interconnection failure

PVFS 1-14vs.01

Appearance  Not connected, broken, burned, corroded or short circuited parts within the junction box. It can
involve solder joints, wires, bypass diodes or tabbing ribbons. The interconnection failure itself
could be hidden by the potting material in the junction box and be visible only by removing the
potting material. The material can appear as degraded (yellowed, browned, burned or bub-
bled) due to the heat or arcing occurring in the junction box.

Detection

IRT, (VI, IV, VOC)

Origin

Impact

Bad contacts or moisture ingress may be the cause of interconnection failures in the junction
box.  Contacts  are  either  soldered,  screwed  or  inserted  (mechanical  spring  clamping).  Bad
soldering contacts are caused by low soldering temperature (cold solder point) or chemical
residuals of the previous production process on the solder joints. Bad mechanical contacts are
caused by loose clamping or screws. Mechanical contacts can get loose due to the thermal
cycling of day and night and seasonal changes. Moisture ingress in bad or damaged junction
boxes (e.g. adhesion loss, brittled, cracked, missing seal at wire entrance or junction box hous-
ing)  leads  to  corrosion  of  the  contacts.  Delamination  near  the  junction  box  can  cause  it  to
become loose, putting mechanical stress on the contacts within the junction box and breaking
them.

Production

Installation

Operation

Bad contacts or corrosion can cause a high resistance and consequent heating in the junction
box.  Resistive  heating  can  moreover  result  in  discolouration  and  burn  marks  in  the
encpasulant/backsheet  behind  and  around  the  junction  box  and  to  glass  breakage.  In the
worst case interconnection failures causes a short circuit or internal arcing within the j-box.
The  heat  can  be  detected  with  a  IR  camera.  In  addition  to  the  visual  defects,  interconnect
failures can also lead to significant power losses, which can be detected by measuring the Voc
of a module or a string. The measurement can be affected by changing mechanical or thermal
stress  conditions.    Interconnect  failures  are  particularly  dangerous  because  the  arcing  can
initiate fire.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

Check  validity  of  IEC  61215
certification and BOM.

Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time.

Testing  of  modules  with  mo-
bile test centre before installa-
tion,  regular  system  inspec-
tion,  installation  of  arc  detec-
tion tool.

79

EXAMPLES (page1)

Examples

1-3

PVFS 1-14vs.01

Junction  box  with  poor  wiring.
[16]

Detached  tabbing  ribbon  due  to
bad soldering. [16]

Corrosion  failure  due  to  water
soaking  of  the  IP65  rated  Jbox.
[41]

Severity

Examples

4-6

Severity

Examples

7-9

Severity

80

Jbox  failure  due  to  poor  electric
connection. [41]

Evidence of loose screw connec-
tion inside Jbox with browning of
pottant. [41]

Cold  soldering  of  module  bus-
sing  ribbon  to  the  Jbox  connec-
tion
terminal  pad  with  minor
browning of pottant.  [41]

Overheating due to the poor Jbox
interconnect  leading  to  light  dis-
coloration and burn mark on front
and back side. [41]

Overheating due to the poor Jbox
interconnect
to  burn
mark and glass breakage. [41]

leading

IR imaging of a hotspot Jbox due
to  loose  electric  connection  in-
side. [41]

Component

Module

Defect

Missing or insufficient bypass diode protection

PVFS 1-15vs.01

Appearance  Missing, disconnected, inverted, damaged, open circuited or short circuited bypass diode.

Detection

BYT, (IV, IRT, EL, STM)

Origin

Impact

Bypass diodes fail either because they are undersized or because they are exposed to high
voltages due to lightning strikes or other high voltage events. In addition to these two reasons,
the diodes have a certain ppm of failure rate, that is the nature of the component. For diodes
working constantly at high temperatures this failure rate increases. Typically, Schottky diodes
are used as bypass diodes in PV modules, but they are very susceptible to static high voltage
discharges and mechanical stress. Two main failure modes are observed with bypass diodes:
open circuit or short circuit. Short circuit condition occurs when the bypass diode is physical
shortened in the junction box, it is mounted the wrong way around or when it has been exposed
to high voltages like lightning strikes or static electricity. Open circuit condition occurs when a
diode is simply missing, it is not properly connected, a strong current damaged the diode, or it
is undersized and not resisting to a continuous current flow.

Production

Installation

Operation

Bypass diodes are mainly used to reduce the power loss caused by partial shading on the PV
module and to avoid the reverse biasing of single solar cells higher than the allowed cell re-
verse bias voltage of the solar cells. In the case of an open circuited diode no current is flowing
through the bypass diode and a cell can be reversed with a higher voltage than it is designed
for the cell and may evolve hotspots that may cause browning, burn marks or, in the worst
case, fire. The problem is that the failure will be not detected until the module is not exposed
to these risks. A short circuited bypass diode will continuously lower the power production of
the module but also of other modules within its string by causing a shift off of their maximum
power point. Bypass diode failures sometimes cause the junction box to deform or even burnt
due  to  heat  dissipated  in  the  junction  box.    When  the  junction  box  or  backsheet  are  burnt
through, the safety issues like leakage current may follow.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules.

Check  bypass  diode  dimen-
sioning,  commissioning  of
system with IRT.

Testing  of  module bypass  di-
odes  with  mobile  test  centre
before  installation.      Regular
IRT inspections.

81

Component

Module

Defect

Not conform power rating

PVFS 1-16vs.01

Appearance  The STC output power of a brand new module is below a specified tolerance limit or the min-
imum nameplate output power is not clearly specified by the manufacturer.

Detection

IV, (MON)

Origin

Deviations of the measured power of a single module respect to the name plate power de-
pends on the product variability, manufacturing quality, the labelling policy and the measure-
ment uncertainty.  The quality of cells (e.g. LID susceptibility) together with the binning method
applied  in  production  for  the  reduction  of  mismatch  losses,  has  a  significant  impact  on  the
product  variability.  The  deviations  in  the  measurement  in  the  factory  comes  from  several
sources of uncertainty, for example the environment temperature, measured module temper-
ature, calibration of the solar simulation, maintenance of the reference module, measurement
equipment, connectors and cables. According to the international standards, the power rating
has to take into account any technology related initial degradation effects (for c-Si see FS 1-
17). This means that after a first exposure to light the output power of a new module has still
to be within the rated power tolerance. The measurement uncertainty of the test laboratory
performing the STC performance test has therefore to be taken into account. The modules
have to be  stabilised  according  the  procedure  described  in  IEC  61215-2:2021.  Technology
specific test requirements are described in IEC 61215-1-1:2021 to IEC 61215-1-4:2021. De-
pending on the technology, a maximum allowable measurement uncertainty is defined for the
verification of power ratings. For c-Si modules it is specified as 3%. A PV module is considered
to be conform to the IEC61215 standard, when following criterion (gate 1) is fulfilled:

Pmax(Lab) ∙ (1 +

1.65
2

|m1|[%]
100

) ≥ Pmax(NP) ∙ (1 −

|t1|[%]
100

)

Pmax (Lab):  measured maximum STC power of each module in stabilized condition
Pmax (NP):    minimum rated nameplate power of each module without rated production tolerances

 m1:    measurement uncertainty in % of laboratory for Pmax (expanded combined uncertainty (k = 2)

   t1 :   manufacturer's rated lower production tolerance in % for Pmax

The minimum nameplate power rating, Pmax(NP) and tolerance t1 has to be derived from the
nameplate or data sheet values. If the Pmax(NP) derived from the datasheet is different from
the nameplate value, the module can be considered to be not conform. If the tolerance is not
stated on the nameplate or the datasheet, then t1 = 0. If the tolerance is not reduced to a single
value  on  the  nameplate  or  data  sheet  (for  example,  if  multiple  tolerances  or  measurement
uncertainty components are specified) the smallest number shall be utilized.

Production

Installation

Operation

Impact

A non-conform STC power rating is not a real module failure, as it causes no degradation or
safety issue, but it has a negative impact on the lifetime energy yield and financial return. An
incorrect estimation of the installed STC power has a direct impact on the energy yield predic-
tions and investor expectations.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Confirm
underperformance
through an accredited PV test
laboratory.  Claim for missing
power.

Verify  power  warranties  and
data  sheet  conformity,  pur-
chase  modules  from  trusted
manufacturers.

Independent  third  party  test-
ing of samples at factory gate
and/or  arrival  on  site.  Signa-
ture  of  a  contractual  agree-
ments.

82

EXAMPLES (page1)

Examples

1

PVFS 1-16vs.01

a)

b)

c)

d)

Example of a hypothetical conform (a-c) name plate and datasheet values with on the right the accord.
IEC 61215-1:2021 derived rated values and tolerances in comparison to a hypothetical example of a
not conform STC rating (d). [IEC 61215-1:2021]

Severity

NA

83

EXAMPLES (page2)

Examples

2

PVFS 1-16vs.01

Statistical analysis done by Eternalsun on around 6500 new modules with 96 different PV module types
from 29 different manufacturers. [35] Considering the measurement uncertainty of +/-2% a total of 4.6%
of the modules are below the gate 1 limit defined by the IEC 61215 standard. [IEC 61215-1:2021]

Note: In case of a measurement uncertainty of +/-5% none of the PV modules would fail, but it would be not conform
to the IEC 61215 standard prescribing a maximum measurement uncertainty for c-Si modules of +/-3%.

Severity

84

Component

Module

Defect

Light induced degradation in c-Si modules (LID/LeTID)

PVFS 1-17vs.01

Appearance  Light induced degradation in crystalline silicon modules is recognisable mainly as a drop in
STC output power, but also short circuit current and open circuit voltage, within the initial life-
time of a PV system. It isn’t correlated with any visual defect or other failure modes. Increasing
non-uniformity of electroluminescence images (patchwork pattern) can in some cases high-
light an ongoing degradation process.

Detection

IV, (EL, IRT)

Origin

Impact

Two different light induced degradation effects are known: LID (light induced degradation) and
LeTID (light and elevated temperature induced degradation). Both degradation modes occur
at cell level, but the physical mechanism staying behind them are different. The first is related
to the concentration of boron and oxygen in the cells, whereas the second one is probably
correlated to the concentration of hydrogen in the cell, but the mechanisms are still not fully
understood.  Mainly p-type multi and mono crystalline silicon modules are affected. High-effi-
ciency cell technologies that use n-type wafers, such as n-type PERC, HJT, or n-PERT seem
to  be  much  less  or  not  at  all  concerned  by  these  two  degradation  effects.  LID  occurs  only
within the first days of exposure to the sun and is limited to 1-3%, whereas LeTID is in a more
severe and long-term light induced degradation mechanism. LeTID was observed for the first
time with the introduction of PERC modules on the market. The degradation can reach up to
10% and sum-up with the LID loss. It occurs only at elevated temperatures above 50 °C. The
speed with which the degradation occurs depends on the average module temperature and is
therefore strongly site dependent. The time frame in which it occurs is in the order of magnitude
of years. Once the full degradation is reached the modules can regenerate, recovering the lost
power. This process is however very slow and also climate dependent. The lost power may
even  not  recover  over  the  typically  expected  25-year  lifetime  of  a  module.  There  exist  ap-
proaches of accelerated regeneration of LeTID-sensitive modules in the field, but they are not
very user-friendly. Over the last years always more manufacturers adapted their cell produc-
tion process to stabilise the cells in-line. Different industrial approaches exist for the mitigation
of LeTID and depending on the methodology the degradation rates, even if reduced, can differ
from one manufacturer to the other and range from 1-4%.

Production

Installation

Operation

LID or LETID causes no safety problems, but it has a negative impact on the lifetime energy
yield and financial return. An under-estimation of the initial degradation has a direct impact on
the  energy  yield  predictions  and  investor  expectations.  LID  is  less  critical  for  the  investors,
because it  is  generally  less severe  and  it  is  taken  into  account  by  the manufacturers  when
labelling the modules and defining the first year warranty, whereas a high LeTID degradation
rate and the difficulty to predict the trend over time is much more critical for manufacturers’
warranties and system owners. The sensitivity of PV modules to LeTID can be tested in the
laboratory. Serious LID above 10% degradation may result in hotspot and can be detected by
IR camera, it happened mainly to the cells produced when PERC were just commercialized
and no mitigation of LID in the manufacturing process was available.

Safety:

Performance:

Mitigation

Corrective actions

Preventive  actions  (recom-
mended)

Preventive actions              (op-
tional)

Confirm
underperformance
through an accredited PV test
laboratory.  Claim for missing
power.

Verify  power  warranties.  Ver-
ify  the  use  of  LeTID  stable
cells by module manufacturer.

Request  test  reports  with  %
power loss for realistic estima-
tions.  Stipulate  a  contractual
agreement  on  tolerated  loss.
Test  individual  modules.  Ver-
ify BOM (cell type).

85

Component

Module

Defect

Insulation failure

PVFS 1-18vs.01

Appearance  A module with bad insulation between its current carrying parts and the frame (or the outside
world) are not directly visible by eye. An unequivocally detection is only possible through a
measurement of the insulation resistance of the module under dry (≥40 Mohm/m²) or better
humid/wet conditions. It can be sometimes deduced by the presence of visual defects which
can potentially lead to insulation problems.  Under certain circumstances like after a rain fall
or in the early morning when the PV modules are covered by dew, this kind of defect is de-
tected by the inverter (low insulation fault) or the inverter is switching off when the resistance
value falls below a certain limit.

Detection

INS, (MON)

Origin

Insulation failures can have different causes. It can occur in the design/production phase of a
module, due to solar cells too closely positioned to the frame or to material weaknesses like
the use of inadequate encapsulation or backsheet materials or a poor lamination process.  In
the installation phase it can be caused by mechanical damages of the module, whereas in the
operational phase it is generally caused by catastrophic events or due to a delamination pro-
cess close to the edge of the module or water ingress or condensation in the junction box.
Modules with failed or skipped insulation test in production due to an insufficient quality as-
surance could be also the origin of the problem.  Various module failures are at the origin of
an insulation failure: backsheet and encapsulant delamination, backsheet damages, burn
marks, glass breakage.

Production

Installation

Operation

Impact

A low insulation resistance at module level itself does not lead to a performance loss, until an
inverter failure occurs. The presence of an electrical leakage current to the frame can become
a safety hazard exposing persons to a potential electric shock hazard. Touching non-insulated
parts of the string or frame can cause severe injury, without the use of safety gear and safe
measuring instruments.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Check  validity  of  IEC  61215
certification  and  BOM,  com-
missioning  of  system  with
IRT,  ground fault detection by
inverter or other devices at all
time.

Regular  system  inspections,
Insulation  testing  of  modules
with mobile test centre before
installation.

Modules with a direct safety
risk or a severity of 5 should
be replaced. Regular inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed modules. In case of in-
dividual  module
testing  all
modules which failed the insu-
lation and/or wet-leakage test
should be replaced.

86

Component

Module

Defect

Hot-spot (thermal patterns)

PVFS 1-19vs.01

Appearance  A  hot-spot  is  a  thermal abnormality  such  as  a  local  overheating  or  a  thermal  pattern  which
deviates from the normal behaviour of a module. It can be detected only by imaging techniques
such as e.g. infrared thermography. Hot spots are not visible by the naked eye until they lead
to irreversible hot-spot damages like e.g. local yellowing, burn marks, glass or cell break-
age. The position, size, intensity and pattern of the hot-spot/s depends on the origin and pro-
gress of the failure, but also under which conditions the module is operating (shading, load
and irradiance level). A temperature gradient of smaller than 10 K is considered as normal and
is not a hot spot or thermal abnormality.

Detection

IRT, (VI)

Origin

Impact

A hot spot may be caused by shading, soiling, severe cell mismatch, damaged cells (e.g. cell
crack and shunted cells), glass breakage, poor electrical connections (e.g. bad or broken sol-
der joints, short circuits, cell interconnect ribbon failures), or low quality solar cell or module
production.  When  such  a  condition  occurs,  the  affected  cell  or  group  of  cells  is  forced  into
reverse bias and will dissipate power, which can cause overheating. If the power dissipation
is high enough or localised enough, the reverse biased cell(s) can overheat resulting in melting
of solder, deterioration of the encapsulant and/or backsheet and glass breakage. To reduce
the effects of hot spots bypass diodes are connected in parallel to the cells. Well-dimensioned
and correctly working bypass diodes helps in reducing hot spot damages from occurring.

Production

Installation

Operation

Hot-spots do not always lead to a power loss. Due to normal tolerances in cell sorting and
module production, thermal abnormalities of less than 10% of the recorded modules usually
do not indicate a special quality issue.  Most of the times modules with a single hot cell have
an  insignificant  power  loss.  Power reduction becomes  significant  when  a  permanently  acti-
vated bypass diode leads to a minimized power output of the affected solar cell string and thus
to a reduction  of  the total  module  power  output.  The  impact  on  system  level  is  only  visible
when more modules are affected. Very high losses can occur when PID is the origin of the
warmer cells. Module safety is affected when the overheating causes critical module damages
or when it leads to a fire. A temperature gradient in a range of 10 K to 20 K is considered as
unproblematic if it is not increasing during the operation of the PV power plant. Temperature
gradients  above  20  K  are  expected  to  cause  power  losses;  in  extreme  cases,  the  material
compound may even degrade, resulting in a safety issue during maintenance work. Further
increase in temperature gradient are expected during the operation phase of the PV power
plant if the modules are not replaced. If PV modules of a system are not cleaned and main-
tained at a suitable frequency, high temperatures of some cells or modules may occur due to
bird droppings or power mismatch for a long time which may lead to module damage. At a
later stage it might be difficult to evaluate whether the damage was caused by quality problems
or by missing cleaning or maintenance procedures.

Safety:

Performance:

Preventive actions
 (recommended)

Preventive actions
(optional)

Commissioning  of  system
with IRT.

Regular system inspections.

Mitigation

Corrective actions

Modules with a direct safety
risk or a severity of 5 should
be  replaced  or  repaired.  If
more than 10% modules show
thermal  abnormalities,
the
reason
that  behaviour
should  be  evaluated  and  re-
spective  corrective  actions
should be implemented.

for

87

EXAMPLES (page1)

PVFS 1-19vs.01

Pattern

Description

Origin

Performance

Remarks

Safety

Power

module
One
warmer than others

Module  is  open
circuited  -  not
connected
to
the system

nor-
Module
mally  fully  func-
tional

Check

wiring

row
(sub-
One
string)
is  warmer
than  other  rows  in
the module

Short  circuited
(SC)  or  open
sub-string
- Bypass diode
  SC, or
- Internal SC

Sub-strings
power lost,
reduction of Voc

May  have  burned
spot at the module

Single  cells  are
warmer,  not  any
pattern  (patchwork
pattern)  is  recog-
nized

Whole  module
is short circuited
-  All  bypass
  diodes SC or
- Wrong
  Connection

Module  power
re-
drastically
duced,
(almost
zero)  strong  re-
duction of Voc

Check wiring

Single  cells  are
lower
warmer,
parts  and  close  to
frame  hotter  than
upper  and  middle
parts.

Massive  shunts
caused  by  po-
tential
induced
degradation
(PID) and/or po-
larization

Module  power
and FF redu-
ced.  Low
performance
more
than at STC

affected

light

- Change array
  grounding
  conditions
- recovery
  by reverse
  voltage

One  cell  clearly
warmer
the
others

than

- Shadowing
 effects
- Defect cell
-  Delaminated
  cell

Power decrease
not  necessarily
permanent,  e.g.
shadowing
leaf
or lichen

Visual inspection
needed, cleaning
(cell mismatch) or
shunted cell

Part  of  a  cell  is
warmer

-  Broken  cell
-  Disconnected
  string
  interconnect

Drastic
reduction,
reduction

power
FF

Pointed heating

- Artifact
- Partly
  shadowed,
e.g.  bird  drop-
ping,
lightning
protection rod

reduc-

Power
tion,
dependent
on
form and size of
the cracked part

Crack  detection
after  detailed  vis-
ual  inspection  of
the  cell  possible

Sub-string  part  re-
markably
hotter
than  others  when
equally shaded

Sub-string  with
missing
or
open-circuit  by-
pass diode

Massive Isc and
power  reduction
when part of this
sub-string
is
shaded

May cause severe
fire  hazard  when
hot  spot  is  in  this
sub-string

Overview of typical IR image patterns observed in outdoor measuerments. [16]

88

(see PVFS 1-15)

(see PVFS 1-10)

(see also PVFS 1-
1, 1-3, 3-3)

(see also PVFS 1-
1, 1-7, 1-9)

(see also PVFS 1-
1, 1-7, 1-9)

(see also PVFS 1-
15, 3-3)

Component

Module

Defect

Soiling

PVFS 1-20vs.01

Appearance  Soiling  is  visible as  a  deposition  of  dust,  dirt  or other contaminants  on the  surface  of  a  PV
module. The deposition can be uniform or non-uniform and vary in thickness. Due to the pres-
ence of hot-spots caused by non-uniform soiling, it can be also seen through IRT imaging.

Detection

VI, (IRT, MON)

Origin

Impact

Soiling of PV modules can have various origins such as dust accumulation, air pollution, bird
droppings or growth of moss, lichens or algae. It can be due to natural sources, as sand in
desert areas, seasonal pollen or volcanic emissions, or due to human activities, as near min-
ing, industry, high ways, railways, urban or agricultural surroundings. The soiling level and its
persistence over time depends on the exposure time, the chemical composition and particle
size as well as the local climate conditions. Whereas rainfalls and wind can lead to a natural
cleaning of modules, humidity can have a contrary effect by increasing adhesion and cemen-
tation of dust on the module. The module design (e.g glass coating, frame, distance of cells
from the edge), the orientation (e.g tilt angle, azimuth, landscape/portrait) and mounting con-
ditions (e.g clamps, height above ground, stringing) of the modules plays an important role.
Typically soiling increases as tilt angles decreases. The direction of the wind or obstacles can
influence the soiling process, leading to non-uniform patterns on system and module level.

Production

Installation

Operation

The deposited soiling layer causes optical losses, reducing the amount of light that reaches
the solar cells, with a consequential performance drop. Soiling is not a real module failure, as
it is reversible when the module is cleaned, but it has a negative impact on the lifetime energy
yield  and  financial  return.  Soiling  is  a  site-specific  issue.  In  arid  regions  with  seasonal  dry
periods  and  dust,  extreme  soiling  losses  of  up  to  25%/a  are  reported,  if  modules  are  not
cleaned. In temperate regions with year-round rain, the annual soiling losses typically ranges
between 0% to 4%. In case of specific soiling sources (e.g. railway, farming, etc.) and/or con-
straints  of  the  natural  cleaning  effect  due  to  unfavourable  mounting  conditions  (e.g  low  tilt
angle) much higher losses can be observed. Non-uniform soiling leads to current mismatch
losses which further increases the power loss and to hot-spots which in extreme cases can
permanently damage a PV module. In modules affected by potential induced degradation
(PID), soiling can further accelerate the ongoing degradation effect. Soiling can be mitigated
by cleaning  the modules  or  preventing  excessive  soiling.  The cleaning  approach has  to be
appropriate to the type of soiling and site specific conditions (e.g. accessibility and water avail-
ability).  The cleaning schedule should take into account that natural agents, such as rain-falls,
wind or dew can have a natural cleaning effect at no cost. Anti-soiling coatings (ASC) can help
in reducing soiling and stretch the cleaning frequency, but only if the coating is adequate for
the type of soiling present on the system and if adequate cleaning processes are followed,
which do not damage the coating. Moreover, it has to be considered that some ASC can also
increase transmission losses by themselves.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Cleaning by qualified persons is
recommended  when  the  reve-
nue lost because of the missed
energy production is higher than
the cleaning cost. A best time to
clean should be defined.

Preliminary  site  inspections
for  the  assessment  of  the
soiling risk. Cost estimation
for  the  implementation  of
mitigation measures. Regu-
lar visual inspections to con-
trol the soiling level.

Estimation or measurement of
soiling losses prior to installa-
tion. Installation of soiling sen-
sors  to  determine  the  most
profitable time to clean.

89

EXAMPLES (page1)

Examples

1-3

PVFS 1-20vs.01

Uniform  light  soiling,  which  in
ideal  conditions  is  self-cleaning
when raining.

Uniform heavy soiling caused by
rail way station. [SUPSI]

Non-uniform  soiling  caused  by
low inclination and close mount-
ing to roof. [SUPSI]

Severity

Examples

4-6

Severity

Examples

7

Severity

90

Moss  growing  on  the  edge  of  a
module combined with edge soil-
ing. [1]

Soiling pattern on a system in the
Atacama desert. [ISE]

Soiling  pattern  demonstrating
dominant wind direction on a test
site in Atacama desert. [ISE]

Heavy biofilm soiling. [46]

Component

Cables and Interconnectors

Defect

DC connector mismatch

PVFS 2-1vs.01

Appearance  Combination  of  male  and  female  DC-connectors  of  two  different  manufacturers  or  types

(cross-mating) between modules, strings, arrays or to the inverter.

Detection

VI, (IRT)

Origin

Impact

There is yet no standard for PV connectors prescribing dimensions and tolerances. Therefore,
it is possible to find very similar-looking and even apparently fitting connectors on the market,
advertised as ‘compatible’.  Slight differences in the design of the connector can lead to re-
duced water and vapour tightness. Problems may also occur due to incompatibilities of mate-
rials (chemical incompatibility or different thermal expansion parameters) of the metal contact,
gaskets  or  sealings.  Most  of  the  time the  mismatch  of  connectors  occurs  at  the  string  end
where extension cables are used or when connecting an inverter or a string combiner box,
which has been delivered with incompatible connectors.

Production

Installation

Operation

The interconnection of connectors from different manufacturers may significantly increase the
risk of loss of performance and defects which cause hazards for human and environment [IEC
TR 63225:2019]. The consequences are e.g. contact corrosion, burnt connectors, electrical
arcing and in the worth case a fire. One of the most common failures is that no current will
flow through the connection at all. The problems do not manifest themselves right away, but
only  over  time  with  increasing  contact  resistance  and/or  degradation  of  the  connector/s.  At
humid weather conditions mismatching connectors can also lead to a partial failure of the in-
verter or a ground fault. The fire risk is further increased when the connectors are not properly
positioned and are close to flammable material such as wooden roof beams or heat-insulation
materials. Often connectors are at least partly installed at position where they cannot be in-
spected during normal visual inspections (e.g. within profiles, underneath roof parallel modules
or even in BIPV). In combination with the unclear compatibility issue, the interconnection of
different brand or type of connectors may result in high risks.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

All  not  matching  connect-
ors should be replaced.

Ask  supplier  or  check  mod-
ule/inverter  spec  sheets  for
the type/manufacturer of con-
nector,  only  connectors  from
the  same  manufacturer  and
certified as compatible should
be mated together.

Verify  that  both  modules  and
inverters  are  delivered  with
the  same  connectors.  Provi-
sion of spare connectors and
string  cables  with  connectors
of the same type as the mod-
ule connectors.

91

EXAMPLES (page1)

Examples

1-2

PVFS 2-1vs.01

Connectors (male of female) are
of different brand or type and ob-
viously do not match. [40]

Connectors (male of female) are
of different brand or type and ob-
viously do not match. [40]

Severity

Examples

3-5

Severity

Examples

6-7

Severity

92

Corroded connector due to cross-
mating. [Stäubli]

Melted  connector  due  to  cross-
mating. [Stäubli]

Burned connector due to cross-
mating. [Stäubli]

Different types of connectors recognisable by dif-
ferent body mouldings and cable gland nuts. [ESV
guide]

Different types of connectors recognisable by dif-
ferent ‘O’ rings or logos. [ESV guide]

Component

Cables and Interconnectors

Defect

Defect DC connector/cable

PVFS 2-2vs.01

Appearance  A damaged connector or cable appear as melted, burned, brittle, broken, cracked or whitened.
Opened connectors can demonstrate corrosion.  Affected connectors show very often over-
heating or hot spots in an early state if a thermography check is performed.

Detection

VI, (IRT)

Origin

One of the major causes of damaged connectors are the combination of incompatible compo-
nents (DC connector mismatch), a low quality connector or a bad installation. In the last case
the connectors are either not installed according the instructions (e.g. bad crimping or connec-
tion, exposure to rain or polluted before installation, installation of damaged connectors) or the
connectors are not fixed correctly exposing them over longer times to humidity or dirt without
allowing the connector to dry completely. In case of damaged cables the major causes are the
use of low quality material in production (e.g. insulation material or cupper wires), an inade-
quate selection of components within the design phase (e.g. undersized cables, too large ca-
ble glands, inadequate IP classification or UV protection)  or an improper handling or fixing of
the cables in the installation phase (e.g. cable routing over sharp or abrading edges, hanging
cables  close  to  connections,  overly  tight  bending,  missing  or  not  correctly  installed  cable
glands or exposure to direct UV radiation).

Production

Installation

Operation

Impact

Damaged connectors or cables constitute a high safety risk and may lead to the power loss of
the whole string. The continuity of the circuit isn’t any more guaranteed and inverter failures
can  occur  (low  insulation  faults  or  inverter  switch  off),  leading  to  partial  or  complete  power
losses. In the worst case damaged cables or not well-connected connectors may cause elec-
tric arcs. In many cases, the connectors and cables are much closer to flammable material
such  as  wooden  roof  beams  or  heat-insulation  materials  than  the  PV  module  laminate,  in-
creasing the risk of fire.

Safety:

Performance:

Mitigation

Corrective actions

Preventive  actions  (recom-
mended)

Preventive actions              (op-
tional)

Components  constituting  a
direct safety risk should be
replaced.  Regular
inspec-
tions should be done to moni-
tor  the  status  of  the  not  re-
placed components.

Protection  of  connectors  and
cables  from  humidity  during
installation.  Use  of  adequate
crimping
Installation
tools.
should  be  done  by  trained
personal.

Signature  of  a  contractual
agreement for maintenance of
the warranty when connectors
are  substituted  by  the
in-
staller,  perform  regular  sys-
tem inspections.

93

EXAMPLES (page1)

Examples

1-3

PVFS 2-2vs.01

Weathered connector. [1]

Cracked connector. [1]

Corroded connector. [1]

Severity

Examples

4-6

Severity

Examples

7

Severity

94

Not  fully  inserted  or  interlocked
connecter. [41]

Melted connector. [1]

Cracked/disintegrated cable in-
sulation. [1]

Incorrect crimping (right) versus correct crimping (left). [47]

EXAMPLES (page2)

Examples

8-10

PVFS 2-2vs.01

Burned connector. [1]

Corroded Cable. [1]

Animal bite on cable. [1]

Severity

95

Component

Cables and Interconnectors

Defect

Insulation failure

PVFS 2-3vs.01

Appearance  A bad isolation of cables is not always visible by eye. An unequivocally detection is only pos-
sible through the measurement of the insulation resistance under dry or humid/wet conditions.
It can be sometimes deduced by the presence of degraded or damaged cables and/or con-
nectors.  Under  certain  circumstances  like  after  a  rain fall  or  in  the  early  morning  when  the
cables or connectors are exposed to humidity, this kind of defect can lead to inverter failures
(low insulation fault or inverter switch off).

Detection

VI, (INS, MON)

Origin

Isolation failures occurs as a result of a short-circuit. It is usually the result of a combination of
humidity and damaged or degraded DC cables or connectors.

Production

Installation

Operation

Impact

A low insulation resistance due to the cables or a connector does not lead to a performance
loss itself, until an inverter failure occurs. An isolation fault can however cause potentially fatal
voltages in the conducting parts of the system potentially exposing persons to an electric shock
hazard. Touching of non-insulated parts may cause severe injury, without the use of safety
gear and safe measuring instruments. In the worst case damaged cables or connectors may
cause electric arcs and initiate a fire.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Cables  or  connectors  con-
stituting a direct safety risk
should be replaced. Regular
inspections should be done to
monitor  the  status  of  the  not
replaced components.

Ground  fault  detection  by  in-
verter  or  other  devices  at  all
time.

Regular system inspections.

96

Component

Cables and Interconnectors

Defect

Thermal damage in combiner box

FS 2-4vs.01

Appearance  Defects  appearing  in  the  combiner  box  as  discoloured  or  burned  cable  interconnections  or

fuses. Damaged parts can be found by visual inspection or infrared thermography (IRT).

Detection

VI, IRT, (MON)

Origin

Thermal damages in the combiner box can be due to the selection of inadequate components
(e.g underrated fuses or fuse holders), a not proper connection of DC cables (e.g  improper
wire torqueing, missing fuses) or a wrong wiring of the modules/strings in the field or on-roof.

Production

Installation

Operation

Impact

This damage is caused by the excess heat generated in fuse holder and defect DC connect-
ors/cables. The partial or complete thermal damage of the combiner box leads to performance
losses, electrical shock hazards and risk of fire. Actions must be taken immediately by qualified
personnel to prevent further damage.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Replace the components with
defect  or  abnormal  tempera-
ture.

Use IRT to check the compo-
nents  and  connection  to  find
poor  connection  or  defect
components.

97

EXAMPLES (page1)

Examples

1-3

FS 2-4vs.01

Burned  terminal  block  of  the
combiner box. [TUV Rheinland]

Improper wire torqueing causes
a fire. [46]

Connection show signs of corro-
sion. [TUV Rheinland]

Severity

Examples

4

Connecting terminals show signs
of  burning,  have  melted  or
charred. [TUV Rheinland]

Severity

98

Component

Mounting

Defect

Bad module clamping

PVFS 3-1vs.01

Appearance

Inadequate fastening or damage of the module or frame by the clamp.

Detection

VI

Origin

Impact

The installation instructions of the module and mounting structure from the manufacturer are
not followed. Typical errors at the planning and installation stage are: (a) use of inadequate
clamps  for  the  selected  module  and/or  mounting  structure,  e.g.  sharp  edges  damaging
glass/glass modules, wrong combination of clamps and modules or mounting structure (b) too
short and too narrow clamps or (c) the positions, kind or number of the clamps on the module
not being chosen in accordance with the manufacturer’s manual. Other errors are too exces-
sively or insufficiently tightened screws during the mounting phase.

Production

Installation

Operation

An improperly installed clamp compromises the integrity of the mounting system and the ability
of the module to stay in place under high wind or load conditions. The detachment of modules
can happen as series effect because the modules share the clamps with the module next to
it. Once one module is detached, the clamp immediately loses fixing force on the next module
and result in series detachment. The detachment of the module/s from the mounting structure
is posing a serious hazard to persons and the risk of damaging the rest of the system and/or
the  property  in  the  vicinity  of  the  installation  site.  Problems  such  as  frame  damage,  glass
breakage or cell cracks can occur compromising on the long term the performance and the
electrical safety.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Modules  with  a  safety  risk
or a severity of 5 should be
replaced.

Use  only  compatible  clamps
(mounting structure/ modules/
clamps)  and  follow  manufac-
turer  mounting
instructions.
Check  local  wind  and  snow
loads.

of

Testing
non-standard
mounting configurations by an
accredited test laboratory (eg.
facade  mounting),  perform
regular system inspections

99

EXAMPLES (page1)

Examples

1-3

PVFS 3-1vs.01

Improper installation of clamp. [?]  Wrong  combination  of  clamps

and modules. [40]

Glass  breakage  caused  by  too
tight screws. [35] (see also PVFS
1-8)

Severity

Examples

4

Glass  breakage  caused  by  poor
[40]  (see  also
clamp  design.
PVFS 1-8)

Severity

100

Component

Mounting

Defect

Inappropriate/defect mounting structure

PVFS 3-2vs.01

Appearance  Mechanical damages (e.g cracking, bending) or other visual defects (e.g. corrosion of frame

or mounting holes) observable on the mounting structure.

Detection

VI

Origin

Impact

Typically, this failure occurs when the mounting structure is not designed to withstand the wind
or  snow  loads  which  are  typical  for  the  site  in  which  the  system  is  installed  (e.g.  mounting
structure does not comply with static calculations, underestimation of the environmental con-
ditions), or if the anchorage of the mounting structure to the ground or roof is weak (e.g. ground
conditions  are  not  considered  sufficiently  when  choosing  the  mounting  structure).  The  roof
strength, to withstand the added load of the PV system and include allowance for O&M activ-
ities, is not verified. Another reason for the failure of a mounting structure is the use of inap-
propriate materials (e.g use of corrosive materials in a corrosive environment, insufficient gal-
vanisation,  poor  quality  material  due  to  a  bad  or  missing  quality  assurance  in  production),
leading to a premature degradation or mechanical failure of the mounting structure. Installation
errors (e.g. missing/non-original components, excessively or insufficiently tightened screws)
can be the origin of a failure of the mounting structure.

Production

Installation

Operation

An inappropriate  or  damaged  mounting  structure  compromises  the  integrity  of  the modules
mounted on it and in some cases also the substructure (e.g roof insulation). In the worst case
this leads to the detachment of single modules or the whole mounting structure from the roof
or ground, or roof collapses, posing a serious hazard to persons and the risk of damaging the
rest of the system and/or the property in the vicinity of the installation site.  Performance losses
are to be expected, depending on the damage on module level (number of disconnected mod-
ules/strings,  glass  breakage,  cell  cracks,  back  sheet  damages,  damaged  or  detached
junction box) and the time and labour needed to repair the system.   Galvanic corrosion is
important for the installation with two different metals in contact, for example aluminium frame
fixed on steel structure, especially in humid or costal area. Direct contact of different metals
generates galvanic corrosion which frequently happens around the fastening screws. There-
fore insulation between two different metals is required in humid and costal area.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Mounting  structures  with  a
direct safety risk should be
replaced or repaired.

Use  only  compatible  mount-
ing structures (ground/mount-
ing  structure/modules)  and
follow manufacturer mounting
instructions. Check local load
(conditions
snow,
other).

(wind,

Regular system inspections.

of

Testing
non-standard
mounting configurations by an
laboratory
test
accredited
(e.g.  facade  mounting),  per-
form  regular  system  inspec-
tions.

101

EXAMPLES (page1)

Examples

1-3

PVFS 3-2vs.01

Corrosion due to salt water. [46]

Cracks in mounting structure due to
mechanical stress. [46]

Screw canal bends due to mechan-
ical stress. [46]

Bracket fractured due to

mechanical stress. [46]

Undersized  mounting  structure
for  local  snow  load  conditions.
[46]

Undersized  mounting  structure
for local wind conditions. [15]

Severity

Examples

4-6

Severity

102

Component

Mounting

Defect

Module shading

PVFS 3-3vs.01

Appearance  Depending on the position of the sun (day and time), shading can be seen either by eye when
performing  a  visual  inspection,  or  by  comparing  monitoring  data  of  unshaded  and  shaded
strings  or  by  running  shading  simulations.  The  shade  can  have  different  patterns  and
change/move over the day and season.

Detection

VI, (MON, IRT)

Origin

Impact

The choice of the mounting structure and the position in which the modules are mounted in-
fluences the shading conditions. Shading can be caused by different factors or obstacles e.g
trees, antennas, poles, chimneys, satellite dishes, roof or façade protrusions, near buildings,
cables, or by self-shading (inter array or row-to-row shading) or soiling. Shading conditions
can change over the lifetime of a PV system due to growing vegetation, new constructions or
construction  elements.  It  can  be  distinguished  between  different  types  of  shades:  direct
shades hindering the direct light to reach the module or diffuse shades.

Production

Installation

Operation

A cell or module which does not receives or receives less sunlight due to a shading obstacle,
lowers the performance of a PV system. Typically, the cumulative annual shading loss of PV
systems is between 1-5%, but energy losses up to 20-30% can be observed for roof top or
façade systems.  Due to series connection of cells and modules, the power loss is significantly
higher than the shaded area. The final loss depends on the on-site implementation or shading
mitigation  measures  like  optimised  string  and  module  arrangements  (landscape  mounting),
use of module-level power electronics (MLPEs), inverter characteristics (MPPT search algo-
rithms, string control) or the use of shading tolerant module technologies (e.g half-cut cells,
back contact cells). Shading itself does not pose a safety issue, but the hot-spots caused by
prolonged shading  can  lead to follow-up failures  (e.g  burn  marks,  bypass  diode failures,
glass breakage, arcing or fire). It further can result in an acceleration of the aging process
resulting into higher degradation rates. The right time to consider the impact of shading is at
the system planning phase, later it is usually too late. The use of MLPEs such as micro-invert-
ers  and  DC  optimizers  for  individual  modules  can  potentially  increase  performance  under
shading conditions, but the gain achieved by these devices do not always exceeds the loss
caused by the MPLE device itself (lower efficiency), and the shading still activates the bypass
diode and result in hot spot on the shaded cell, which increases the risk of reliability issues.
The  choice  of  using  them  only  in  the  area  where  shading  occurs  should  be  considered  an
alternative to install them for all modules. A cost benefit analysis should be done in any case.

Safety:

Performance:

Mitigation

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Indirectly  damaged  mod-
ules with a safety or sever-
ity  risk  of  5  should  be  re-
placed or repaired.  Eventual
trees  or  vegetation  responsi-
ble for the increased shading
loss should be cut.

A basic shading analysis (full
year solar/shade data) is rec-
ommended  to  identify  areas
and periods of major shading.
Areas  exposed  to  shading
within  the  central  part  of  the
day  or  sunny  season  should
be  avoided  or  appropri-
ate/cost-effective shading mit-
igation measure should be im-
plemented.

A detailed shading loss analy-
sis should be done which esti-
mates and compares different
system  configurations  and
shading mitigation measures.
Perform  regular  system  in-
spections.

103

EXAMPLES (page1)

Examples

1-3

PVFS 3-3vs.01

Shading  by  pole-and-wire  (poor
design: too close to nearby shad-
ing objects). [36]

Shading  due  to  bad  planning  or
coverage by afterwards build con-
struction element. [40]

Shading  by  tree  with  seasonal
changes due to foliage. [40]

Severity

Examples

4-6

Severity

Examples

7

Severity

104

Missing  maintenance  on
green roof. [SUPSI]

flat

Vertical  shading  of  a  standard
module  with  3  bypass  diodes.
[J.Lin]

Shading by balustrade. [J.Lin]

Continuous  shading  caused  by
chimney. [SUPSI]

Component

Inverter

Defect

Overheating

PVFS 4-1vs.01

Appearance  The inverter reduces its power or switches off to protect components from overheating (tem-
perature derating). Inverters do not always deliver a corresponding status message "power
reduction" or "derating". For this reason, it is recommend to check the inverter behaviour by
determining and analysing performance curves (Power vs Irradiance).

Detection

MON, (IV, IRT)

Origin

Impact

Temperature derating of the inverter can occur for various reasons, e.g. improper installation
of the inverter, fan failure, dust blocking heat dissipation or an incorrect programming of the
inverters.

Production

Installation

Operation

When the monitored components in the inverter reach the maximum operating temperature,
the inverter shifts its operating point to a lower power. During this process, power is reduced
step-by-step. In the extreme case, the inverter switches off completely. As soon as the tem-
perature of the threatened components falls below the critical value, the inverter returns to the
optimal operating point. The partial or complete failure of the inverter leads to performance
losses, which will get worth if the problem is not solved. In the worth case inverter will switch
off. Inverter overheating do not affect module safety.

Safety:

Performance:

Action

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Once identified the origin of
the temperature derating the
failure should be repaired.
The filters and in general
heat dissipation path should
be cleared of obstruction.

Follow  the  given  installation
procedure,  use  of  adequate
cooling  technology,  perform
regular inspections of the ven-
tilation units.

Monitoring of inverter temper-
ature

105

EXAMPLES (page1)

Examples

1-3

PVFS 4-1vs.01

Dust blocking heat dissipa-
tion [TUV Rheinland]

A soiled air filter causes over-
heating [TUV Rheinland]

Installation not appropriate
(direct exposition to sun)
[TUV Rheinland]

Severity

106

Component

Inverter

Defect

Incorrect installation

PVFS 4-2vs.01

Appearance  The inverter must be installed according to the installation instruction. A common failures is
the installation near flammable, explosive, corrosive or humid sources. Also the minimum dis-
tances to bottom, top or to the sides are not always fulfilled. If the input cables are not fixed
properly,  increased  temperatures  can  occur  at  the  loose  contact  point  which  lead  to  lower
performance or risk of fire. Inverters must always be accessible for operation and maintenance
and properly secured to an appropriate base.

Detection

VI (MON)

Origin

Impact

Violating  instruction manual,  e.g.  installed  nearby  flammable materials  as  wood  or  in direct
sun light.
Minimum distance to adjacent components not maintained.

Production

Installation

Operation

Incorrect installation of the inverter can cause danger to users and hazardous conditions and
can result in overheating of the inverter. The use of the inverter in the presence of flammable
vapours or gases can lead to explosions. The inverter housing can  become very hot under
operation. Follow the instruction to provide gaps from both sides and top for adequate cooling.
Direct  sunlight  on  the  inverters  must  be  avoided. The  inverter  must  be  safely  accessible to
avoid accidents during maintenance work.

Safety:

Performance:

Action

Corrective actions

Preventive actions
 (recommended)

Preventive actions
(optional)

Dismount the component and
follow the installation proce-
dure.

Follow  the  given  installation
procedure,  use  of  adequate
cooling  technology,  perform
regular inspections of the ven-
tilation units.

Monitoring of inverter temper-
ature.

107

EXAMPLES (page1)

Examples

1-3

PVFS 4-2vs.01

Installation in direct sun light.
[TUV Rheinland]

Inverters are not or difficult ac-
for  operation  and
cessible
maintenance.
[TUV  Rhein-
land]

Distance  to  bottom,  top  or  to
the sides too low. [TUV Rhein-
land]

Housing
[TUV Rheinland]

not

appropriate.

Presence of inflammable ma-
terial. [SUPSI]

Severity

Examples

4-5

Severity

108

Component

Inverter

Defect

Not operating (complete failure)

PVFS 4-3vs.01

Appearance

If the inverter does not work despite good production conditions, common problems are the
lack of restart after grid faults or isolation faults. The inverter may show fault codes to help
understanding the problem. This can be observed by checking the display or the data log of
the  monitoring  system.  Examples  for  hardware  defects  in  the  inverter  are  discoloured  or
burned cable interconnections or fuses. Damaged parts can be found by visual inspection or
infrared thermography (IRT).

Detection

MON, (VI, I-V, VOC)

Origin

Impact

A complete failure of the inverter occurs due one or more malfunctions of single hardware or
software component of the inverter or faults due to grounding issues, e.g. high humidity inside
the inverter, or a firmware issue.

Production

Installation

Operation

The  complete failure  of  the  inverter  leads  to  significant  performance  losses  and  immediate
actions must be taken. When the restart does not work or the fault occurs recurrently the origin
must be identified in most cases by a service team. Software issues can be solved by updating
the  firmware  for technical  reasons  or  to  update the  system  to  new  standards/grid technical
requirements. While damaged hardware components of central inverters are usually repaired,
string inverter are replaced more often for economic reasons. Damaged hardware can cause
fire and electric shock hazards and must be repaired by qualified personnel.

Safety:

Performance:

Action

Corrective actions

Preventive actions
(recommended)

Preventive actions
(optional)

Restart  the  inverter.  Replace
the components with defect or
abnormal
temperature.  Up-
date the software.

Use IRT and VOC to check
the components and connec-
tion to find poor connection or
defect components.

109

EXAMPLES (page1)

Examples

1-3

PVFS 4-3vs.01

Insulation failure. [TUV
Rheinland]

Not  operating  inverter.  [TUV
Rheinland]

Damaged  hardware  compo-
nent. [37]

Severity

110

111


