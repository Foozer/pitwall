# Pitwall

## Summary

Pitwall is a command line tool that lest you quickly check Formula 1 race weekend schedule, driver standing and race results directly from the terminal.

It fetches live data drom an F1 API and presents it in a clean CLI interface.

Perfect for F1 fans who want quick race infor without opening a browser.

## Examle Usage

```
python3 pitwall next
```
Output:
```
Next Race: Japanese Grand Prix
Track: Suzuka Circuit

Practice 1: Fri 03:30
Practice 2: fri 07:00
Practice 3: Sat 03:30
Qualifying: Sat 07:00
Race: Sun 06:00
```

```
python3 pitwall standings
```

Output:
```
Driver Standings

1. Max Verstappen - 410 pts
2. Lando Norris - 315 pts
3. Charles Leclerc - 289 pts
4. Lewis Hamilton - 230 pts
```

```
python3 pitwall driver hamilton
```

```
Lewis Hamilton
Team: Mercedes
Wins: 103
Podiums: 197
Championships: 7
```
