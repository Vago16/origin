### Conceptual Exercise

Answer the following questions below:

- What is Redux? Why might you use it?
  
Redux is a state management library for JavaScript apps. It allows you to manage the state of your application in a central location, rather than having to manage it in multiple places.

- What are three features of the Redux developer tool in Chrome?
  
The Redux developer tools allows the developer to see the state of the application and allows them to view the history of actions that have been dispatched.

- What is a store?
  
A store is a container for the state of your application.

- What is a reducer?

A reducer is a function that takes the current state and an action, and returns the new state.

- What is an action?
  
An action is an object that accepts a type that tells the reducer how to process the state.

- What is an action creator?
  
An action creator is a function that returns an action object.

- How does data flow in a React/Redux application?
  
In a React/Redux application, the data flows from components to the store by use of a dispatch method. The dispatch method then invokes the reducer, which updates the state. The state can then be interpreted by any component needs it.

- What is the purpose of the `<Provider>` component?
  
A provider component provides all child components access to the store.

- What is the purpose of the `useSelector` hook? What does it return?
  
The useSelector hook allows you to access states in your store. A callback is passed as a parameter to the hook, which then describes how to return information from the store.

- Describe the `useDispatch` hook. What do you use it for?
  
The useDispatch hook returns a callback that can be used to dispatch actions.

- What is redux-thunk and why would you use it?

redux-thunk is a library that simplifies the process of dispatching asynchronous actions, such as those that rely on an external API.

- What are propTypes?
  
propTypes is a react library that lets you strictly define what kind of objects a component accepts as props.

- Describe the `useCallback` hook.  What is it used for?
  
useCallback is a hook that allows you to memorize a callback function. This is useful for two reasons: First, it helps performance by preventing the callback function from being recreated every render. Secondly, it allows you to use this function as a dependency in a hook, avoiding an infinite loop.

- Compare and contrast the `useReducer` hook with Redux (including react-redux).  Why would you choose one over the other?

Redux's reducer allows middleware, which allows you to use libraries that simplify the process of managing state. React's useReducer allows no such thing, which makes it harder, for example, to manage states with asynchronous callbacks.