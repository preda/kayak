#!/usr/bin/python3

times = [38.590, 107.046, 230.5, 33.741, 95.544, 204.006]

def format(t):
  m = t // 60
  s = t - m * 60
  return f"{m:.0f}:{s:02.0f}" if m else f"{s:.1f}"

def line(percent):
  r = percent / 100
  s = "<tr>"
  s += f" <td>{r:4.0%} </td>"
  for t in times[0:3]:
    s += " <td> " + format(t / r) + " </td>"
  s += " <td> </td>"
  for t in times[3:6]:
    s += " <td> " + format(t / r) + " </td>"
  s += f" <td>{r:4.0%} </td>"
  s += "</tr>"
  return s
    
print(
'''<!DOCTYPE HTML>
<html>
<head>
<style>
table th { padding: 10px; border-spacing: 0px; }
table tr:nth-child(odd) td {
  background:#fff;
}
table tr:nth-child(even) td{
}
.W { background-color: #fef }
.M { background-color: #eff }
</style>
</head>
<body style='text-align:center'>
<table border="0" style="border-collapse: collapse; margin-left:auto; margin-right:auto;" >
<colgroup>
<col class='W'>
<col class='W'>
<col class='W'>
<col class='W'>
<col>
<col class='M'>
<col class='M'>
<col class='M'>
<col class='M'>
</colgroup>
<tr><th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th> <th>WK1 200</th> <th>WK1 500</th> <th>WK1 1000</th> <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th> <th>MK1 200</th><th>MK1 500</th><th>MK1 1000</th> <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><tr>
'''
)

print(line(100))
for p in range(90, 69, -1):
  print(line(p))

print(
'''
</table>
</body>
</html>
'''
)
