# NBA All Star Team Selection Classifier
This application leverages a Decision Tree Classifier fed with the data of the Top-100 NBA players from the 2015-2016 NBA regular season, to the 2019-2020 NBA regular season. The set of player statistics drawn from this source of data is restricted to the dates starting from the beginning of the season up until the day that the player's respective All Star Team selection is made.

The code base additionally consists of a web scraper to pull each players' respective stats from the BasketballReference website.

## Version 1.0
At the end of the initial phase of development, we've produced the classification trees for players across four categories:

| Guard | Forward | Point-Forward | Center |

The NBA All Star team selections are made with respect to two major categories: Frontcourt and Backcourt. In the NBA, there are five player positions - Point Guard, Shooting Guard, Small Forward, Power Forward, and Center. Frontcourt refers to players from the Forward positions, as well as centers. Backcourt refers to players from the Guard positions.

The problem with sticking to the two major categories is that the classifier will be essentially be fed data with a substantially high variance in regards to the Frontcourt category, considering the constrasting roles that players fitting this category ultimately demonstrate on the court. As a result, the Frontcourt category was dissolved into two subcategories: Forward and Center. At this point, we've dissolved the initial set of categories into a more fine-tuned set consisting of: Guard, Forward, and Center.

Another issue arises with this set of three categories, in that several of the elite players in the NBA are capable of playing multiple positions. Players such as LeBron James come to mind - capable of guarding all five positions, elite playmaking skills to facilitate a team's offense, having an established presence in the post, and additionally able to rebound effectively. His frame is fitting of a modern-day Power Forward, but was considered a Small Forward prior to this current era of basketball. Players that typically fit an eclectic description like "The King" are referred to as a Point-Forward. Their stats tend to be relatively well-rounded compared to their positional counterparts. Examples include players like Giannis Antetokounmpo and Draymond Green - both listed as Power Forwards for their teams, and both whom take significant playmaking responsibilities within their teams, which can be reflected in their higher than average assist numbers. The Point-Forward archetype is just one of many "Tweener" references made in basketball.

In a future release, we plan to expand the number of categories corresponding to the aforementioned "Tweener" archetypes. Stay tuned!
