copy theme(ApplicantNo, Age, EdLevel, Gender, MainBranch, YearsCode,
           Country,HaveWorkedWith,ComputerSkills)
from '/docker-entrypoint-initdb.d/seed_data/job_applicant_data.csv'
delimiter ','
csv header;

