-In action creators, like getFilmFromAPI, we use a "regular expression" --- what is that regular expression, and what is its purpose?

This regular expression is used to extract the film ID from the URL. It uses a /d+/ match which will match any number of digits.

-We're persisting the Redux store, so if you re-visit the app, it will remember the topics you've visited. Where is this stored? How is this done?

Redux-persist stores the store in the local storage of the browser. Redux persist works as middleware that wraps the entire application one level under the the Provider. This uses a persist gate.

-What does combineReducers do? Why are we using it?

Combine reducers lets you use multiple reducers spread out across multiple files. This allows you to have a single store that is made up of all different parts of the application. It allows us to make our core more modular and neater.

-How does the "Reset to Fresh Exploration" feature work?
The reset all dispatches an action that returns all stores to the default states.

-Why are FilmList.js, PlanetList.js, and PersonList.js all simple components that use an ItemList? Why is this a good design?
The ItemList is a simple and reusable component. It is used in all 3 places and all one has to do is populate the list with the correct data.

-In the HomePage component we use the useSelector hook to save only a single fact--- whether the first film is loaded, We could instead have selected all the films, and had the check for whether the first film is loaded in our render function. Why is this worse? What would the performance implications be?
If we had selected all the films, the useSelector hook would've potentially forced more unnecessary renders. To this end we are only checking for one film and not all of them.

-What good ideas for designing and organizing React apps have you learned from studying this code?
I have learned how to use an external library to keep our states persistent across refreshes. I have also learned how to structure a proper store.

-Which Star Wars character would make the best React developer, and why?
Probably Anakin Skywalker as he has experience with hardware and software building robots.