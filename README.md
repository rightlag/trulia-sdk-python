```python
from trulia import build


def main():
    service = build('TruliaStats', '<YOUR_TRULIA_API_KEY>')
    res = service.get_city_stats(city='New York', state='NY')
    print res.location
    for traffic_stat in res.traffic_stats:
        print traffic_stat.percent_state_traffic

if __name__ == '__main__':
    main()
```
