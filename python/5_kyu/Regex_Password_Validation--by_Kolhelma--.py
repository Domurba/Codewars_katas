#2021-11-06 16:20:33.700000+00:00
"""You need to write regex that will validate a password to make sure it meets the following criteria:

  <ul>
    <li>At least six characters long</li>
    <li>contains a lowercase letter</li>
    <li>contains an uppercase letter</li>
    <li>contains a number</li>
  </ul>
  
Valid passwords will only be alphanumeric characters."""

regex="^(?=[0-z]*[a-z])(?=[0-z]*[A-Z])(?=[0-z]*[0-9])[a-zA-Z\d]{6,}$"