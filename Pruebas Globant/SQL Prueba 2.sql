select
w.department 
,w.job
,sum(w.Q1) as Q1
,sum(w.Q2) as Q2
,sum(w.Q3) as Q3
,sum(w.Q4) as Q4
from(
select
y.name as department
,z.name as job
,substr(left(date,10),6,2)
, Case 
    when substr(left(date,10),6,2)>=1 and substr(left(date,10),6,2)<= 3 then 1 else 0
  end as Q1
, Case 
    when substr(left(date,10),6,2)>3 and substr(left(date,10),6,2)<= 6 then 1 else 0
  end as Q2
, Case 
    when substr(left(date,10),6,2)>6 and substr(left(date,10),6,2)<=9 then 1 else 0
  end as Q3
, Case 
    when substr(left(date,10),6,2)>9 and substr(left(date,10),6,2)<= 12 then 1 else 0
  end as Q4
 from hired_employees x
left join departments y on x.deparment = y.id
left join jobs z on x.job= z.id) w
group by department,job
order by department desc;