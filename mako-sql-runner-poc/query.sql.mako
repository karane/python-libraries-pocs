<%!
# Define a list inside the template
roles = ["admin", "editor", "viewer"]
%>

SELECT *
FROM users
WHERE 1=1

AND role IN (
% for i, r in enumerate(roles):
    '${r}'${"," if i < len(roles) - 1 else ""}
% endfor
)

ORDER BY id
LIMIT ${limit or 50};
