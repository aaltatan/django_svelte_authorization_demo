<script>
  import Home from "./pages/Home.svelte";
  import About from "./pages/About.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import Admin from "./pages/Admin.svelte";
  import Router, { link } from "svelte-spa-router";
  import AuthorizationWrapper from "./components/AuthorizationWrapper.svelte";
  import { beforeUpdate } from "svelte";
  import { userPermissions } from "./stores/user";
  import { onlyFor, has } from "./utils/permissions";

  beforeUpdate(() => {
    let perms = JSON.parse(
      localStorage.getItem("permissions").replaceAll("&quot", '"').replaceAll(";", "")
    );
    userPermissions.set(perms);
  });

  const routes = {
    "/": Home,
    "/about": About,
    "/admin": Admin,
    "*": NotFound,
  };
</script>

<div>
  <header>
    <nav>Hello World!</nav>
    <ul>
      <li><a href="/" use:link>Home</a></li>
      <li><a href="/about" use:link>About</a></li>
      <AuthorizationWrapper permissions={onlyFor("customer", has.ADD | has.VIEW)}>
        <li><a href="/admin" use:link>Admin</a></li>
      </AuthorizationWrapper>
    </ul>
  </header>
  <main>
    <Router {routes} />
  </main>
  <footer></footer>
</div>
