# Classic Cookie Challenge
### [Problem description here.](https://youtu.be/a4Py6rrf2Dk)


## Problem Description:
Given a cookie in matrix structure, where elements of the matrix are either 1 or 0  representing :

| element |   description   |
| ------- | --------------- |
|   `1`   | a chocolate chip|
|   `0`   |    other part   |

You have to find all the number of chocolate chips in each groups which are there in the chocolate cookie.  
Chocolate cookies are grouped together when they share one edge common between them. 
that is for a piece of cookie chip, possible grouping elements are:
   - [x] top
   - [x] left
   - [x] right
   - [x] down
   - [ ] diagonal
   
  
  
  
<table>
<tr><th>Cookie</th><th>Matrix representation</th><td rowspan=6>When chocolate chip is represented by 1.</td></tr>
<tr><td>

|   |   |   |   |   |   |
| - | - | - | - | - | - |
| &#9634;  | &#11044; | &#9634;  | &#9634;  | &#9634;  | &#9634;  |
| &#9634;  | &#11044; | &#9634;  | &#9634;  | &#9634;  | &#9634;  |
| &#11044; | &#9634;  | &#11044; | &#11044; | &#9634;  | &#11044; |
| &#9634;  | &#11044; | &#11044; | &#9634;  | &#11044; | &#11044; |
| &#11044; | &#9634;  | &#9634;  | &#11044; | &#9634;  | &#9634;  |
| &#9634;  | &#9634;  | &#9634;  | &#9634;  | &#9634;  | &#9634;  |

</td><td>

|   |   |   |   |   |   |
| - | - | - | - | - | - |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 |

</td></tr> </table>    


#### Result of grouping:    
![table](https://user-images.githubusercontent.com/20074475/50734125-cdc24f00-11bf-11e9-8c7c-dc31fa452fa2.png)

Answer of above example would be:
<pre>[1, 1, 1, 2, 3, 4]</pre>
