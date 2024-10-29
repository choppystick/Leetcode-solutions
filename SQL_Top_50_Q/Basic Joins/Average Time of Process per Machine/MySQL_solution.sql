-- MySQL solution for Average Time of Process per Machine

select start.machine_id, round(avg(end.timestamp - start.timestamp), 3) processing_time
from Activity start JOIN Activity end
    on start.machine_id = end.machine_id 
    and start.process_id = end.process_id 
    and start.activity_type = "start"
    and end.activity_type = "end"
group by start.machine_id



