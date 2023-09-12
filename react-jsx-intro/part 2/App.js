function App() {
    return (
        <div>
        <Tweet
          name="Samantha"
          username=" samanthacoolgirl "
          date={new Date().toDateString()}
          message="Im a cool girl"
        />
        <Tweet
          name="Anonymous"
          username=" anon "
          date={new Date().toDateString()}
          message="Hey guys I love having secrets"
        />
        <Tweet
          name="Michael Jackson"
          username=" ThrillerBadBoi "
          date={new Date().toDateString()}
          message="hehe they tried to fake my death but I'm still alive hehe"
        />
      </div> 
    );
}