select x.*
		,count(y.id) as hired
        
from departments x
left join hired_employees y on x.id = y.deparment
group by id,name
order by hired desc ;

