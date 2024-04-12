<script>
  import { userPermissions } from "../stores/user";
  import { afterUpdate } from "svelte";

  export let permissions;

  let canAccess = false;

  afterUpdate(() => {
    userPermissions.subscribe((value) => {
      canAccess = permissions.length && permissions.every((el) => value.includes(el));
    });
  });
</script>

{#if canAccess}
  <slot />
{/if}
