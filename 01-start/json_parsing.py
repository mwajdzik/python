import json
import urllib.request


def print_results(data):
    js = json.loads(data)

    if 'title' in js['metadata']:
        print(js['metadata']['title'])

    print(str(js['metadata']['count']) + ' events recorded\n')

    for i in js['features']:
        print(i['properties']['place'])

    print('\n-------------------------------------\n')

    for i in js['features']:
        if i['properties']['mag'] >= 4.0:
            print('%2.1f:' % i['properties']['mag'], i['properties']['place'])

    print('\n-------------------------------------\n')

    print('Events that were felt:')
    for i in js['features']:
        felt_reports = i['properties']['felt']
        if felt_reports is not None and felt_reports > 0:
            print('%2.1f:' % i['properties']['mag'], i['properties']['place'],
                  'reported ' + str(felt_reports) + ' times')


def main():
    url_data = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    web_url = urllib.request.urlopen(url_data)
    code = web_url.getcode()

    print('result code: %d\n' % code)

    if code == 200:
        print_results(web_url.read())
    else:
        print('Received an error from server, cannot retrieve results ' + str(code))


if __name__ == '__main__':
    main()
