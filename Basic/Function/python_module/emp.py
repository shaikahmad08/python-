#type-1 using import
import user
print(user.empid)
print(user.empname)

#type-2 using aliasing
from user import empid as eid,empname as ename
print(eid)
print(ename)