import pandas as pd
import numpy as np
import matplotlib as plt


food = pd.read_csv('C:/Users/Sergei/Downloads/Fig3-1.xls')

print(food)

# Restaurant_id — идентификационный номер ресторана / сети ресторанов;
# City — город, в котором находится ресторан;
# Cuisine Style — кухня или кухни, к которым можно отнести блюда, предлагаемые в ресторане;
# Ranking — место, которое занимает данный ресторан среди всех ресторанов своего города;
# Rating — рейтинг ресторана по данным TripAdvisor (именно это значение должна будет предсказывать модель);
# Price Range — диапазон цен в ресторане;
# Number of Reviews — количество отзывов о ресторане;
# Reviews — данные о двух отзывах, которые отображаются на сайте ресторана;
# URL_TA — URL страницы ресторана на TripAdvisor;
# ID_TA — идентификатор ресторана в базе данных TripAdvisor.