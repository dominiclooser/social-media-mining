import numpy as np
from matplotlib import pyplot as plotter
from pattern.web import Twitter
import pandas as pd

from apis.flickr_api import flickr
from apis import instagram_api, flickr_api


pd.options.display.mpl_style = 'default'


def tags_for_place(woe_id):
    response = flickr.places.tagsForPlace(woe_id=woe_id)
    print(response)


def find_place(query):
    response = flickr.places.find(query=query)
    print(response)


def sandbox():
    params = flickr_api.get_params('switzerland')
    photos = flickr_api.get_photos(params)
    print photos.get_size()


def walking():
    params = flickr_api.get_params('switzerland')
    params['min_upload_date'] = '2015-01-01'
    # params['per_page'] = 1000
    photos = flickr_api.get_photos(params)
    print photos.total


def array():
    x = [1, 2, 3]
    y = [1, 4, 9]
    data = numpy.array([x, y])
    numpy.savetxt('test.csv', data, fmt='%g')
    loaded = numpy.loadtxt('test.csv')
    x = loaded[0]
    y = loaded[1]
    plotter.plot(x, y)
    plotter.show()
    print data


def facebook():
    api = Twitter()

    results = api.search('Hochwasser')
    print len(results)
    for result in results:
        print dir(result)
        break


def pandas():
    index = range(2004, 2015)
    data = np.random.randn(len(index))
    series = pd.Series(data, index=index)
    series.plot()
    plotter.show()


def pandas_plotting():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plotter.show()


def instagram():
    popular_media = instagram_api.api.media_popular(count=20)
    for media in popular_media:
        print media.images['standard_resolution'].url

if __name__ == '__main__':
    print flickr_api.count_photos(flickr_api.Query.switzerland)

