SELECT  myAdds.[Product Code],myAdds.[Item No],myAdds.[Title],myAdds.[Internet Category ID],myAdds.[Price],myAdds.[Length],
myAdds.[Width],myAdds.[Weight],myAdds.[Image Link],myAdds.[Ad Copy],myAdds.[Seasonal],myAdds.[Closer Look ID]
INTO UPDATES
from myAdds
INNER JOIN myDeletes
On myAdds.[Item No] = myDeletes.[Item No]
