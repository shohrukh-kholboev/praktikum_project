from django.urls import path
from .views import (
    news_detail,
    errorPageView,
    ContactPageView,
    HomePageView,
    NewsListView,
    LocalNewsView,
    ForeignNewsView,
    TechnologyNewsView,
    SportNewsView,
    NewsUpdateView,
    NewsDeleteView,
    NewsCreateView,
    admin_page_view,
    SearchResultsListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home_page'),
    path('news/', NewsListView.as_view(), name='all_news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name = 'news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name = 'contact_page'),
    path('error/', errorPageView, name = 'error_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('search-result/', SearchResultsListView.as_view(), name='search_result')
]