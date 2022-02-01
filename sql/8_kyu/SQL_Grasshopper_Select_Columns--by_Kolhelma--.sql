#2021-09-16 13:22:28.806000+00:00
"""#Greetings Grasshopper!#
Using only SQL, write a query that returns all rows in the custid, custname, and custstate columns from the customers table.
**********************************************************************
###Table Description for customers:###
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#aaa;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#fff;background-color:#303133;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aaa;color:#fff;background-color:#79a0dd;}
.tg .tg-yw4l{vertical-align:top}
</style>
<table width=700 class="tg">
  <tr>
    <th class="tg-031e">Column</th>
    <th class="tg-031e">Data Type</th>
    <th class="tg-031e">Size</th>
    <th class="tg-031e">Sample</th>
  </tr>
  <tr>
    <td class="tg-031e">custid</td>
    <td class="tg-031e">integer</td>
    <td class="tg-031e">8</td>
    <td class="tg-031e">4</td>
  </tr>
  <tr>
    <td class="tg-031e">custname</td>
    <td class="tg-031e">string</td>
    <td class="tg-031e">50</td>
    <td class="tg-031e">Anakin Skywalker</td>
  </tr>
  <tr>
    <td class="tg-yw4l">custstate</td>
    <td class="tg-yw4l">string</td>
    <td class="tg-yw4l">50</td>
    <td class="tg-yw4l">Tatooine</td>
  </tr>
  <tr>
    <td class="tg-yw4l">custard</td>
    <td class="tg-yw4l">string</td>
    <td class="tg-yw4l">50</td>
    <td class="tg-yw4l">R2-D2</td>
  </tr>
</table>

***
Your solution should contain only SQL.   
   
      
         """

select custid, custname, custstate  from customers