<h1>Routing</h1>

<h2>Routing Engine</h2>

There is currently only the one routing engine for the framework, this uses regex to find the matches in the routing path


    from routing.routing_engine import RoutingEngine, HostRoute, UriRoute
    
    routing = RoutingEngine()
    routing.append(
        HostRoute(
            'localhost:8081',
            [
                UriRoute('/this', working_routing),
                UriRoute('/', welcome)
            ]
        )
    ) 
    
As can be seen from the above once the routing engine is instantiated the routes are appended, the routing structure must be a host 
route containing uri routes. Also please note that routes are first match return so order your routes to be most specific first. 