#2021-10-10 12:09:27.334000+00:00
"""For this challenge you need to create a VIEW. This VIEW is used by a sales store to give out vouches to members who have spent over $1000 in departments that have brought in more than $10000 total ordered by the members id. The VIEW must be called `members_approved_for_voucher` then you must create a SELECT query using the view.

## Tables and relationship below:
<image src="http://i.imgur.com/hkEkGg1.png">

### resultant table schema
- id
- name
- email
- total_spending

> NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing."""

CREATE VIEW members_approved_for_voucher as
SELECT m.id, m.name, m.email, sum(p.price) as total_spending
FROM sales s
JOIN members m ON m.id = s.member_id 
JOIN products p ON p.id = s.product_id
  JOIN (SELECT d.id 
  FROM departments d
  JOIN sales s on d.id = s.department_id
  JOIN products p on p.id = s.product_id
group by d.id
HAVING sum(p.price) > 10000) d on d.id = s.department_id
group by m.id
having sum(p.price) > 1000;

select * from members_approved_for_voucher order by id

