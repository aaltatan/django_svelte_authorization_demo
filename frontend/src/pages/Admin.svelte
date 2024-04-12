<script>
  import { has, onlyFor, redirectUnauthorizedUser } from '../utils/permissions';
  import { userPermissions } from '../stores/user';
  import { onMount } from 'svelte';

  const pagePermissions = onlyFor('customer', has.ADD | has.VIEW);

  onMount(() => {
    redirectUnauthorizedUser(userPermissions, pagePermissions);
  })

</script>

<div>
  Admin Page
</div>