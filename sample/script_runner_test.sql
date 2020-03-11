
drop table if exists  zzztemp;

create table zzztemp (
  dt timestamp,
  var varchar,
  from_date timestamp,
  batch_no integer
  );

insert into zzztemp
values (getdate(), '$[?var1]', '$[?from_date]', '$[?batch_no]');

insert into zzztemp
values (getdate(), '$[?var2]', '$[?from_date]', '$[?batch_no]');

select * from zzztemp;
commit;
