<script>
  import { location } from 'svelte-spa-router';
  import { onlyFor, has } from '../utils/permissions';
  import AuthorizationWrapper from '../components/AuthorizationWrapper.svelte';
</script>

<main>
  Home Page {$location}
  <AuthorizationWrapper permissions={onlyFor('customer', has.ADD | has.DELETE)}>
    <h1>this text is for Authorized users only</h1>
  </AuthorizationWrapper>
  <h1>this text is for ALL</h1>
</main>