import { pop } from "svelte-spa-router";

export function onlyFor(
  singleName,
  permissions = 15,
  appName = "",
  defaultPerms = ["view", "add", "change", "delete"]
) {
  appName = appName ? appName : singleName + "s";
  return permissions
    .toString(2)
    .padStart(defaultPerms.length, "0")
    .split("")
    .map((el, idx) => (+el ? `${appName}.${defaultPerms[idx]}_${singleName}` : ""))
    .filter((el) => el);
}

export const has = {
  VIEW: 8,
  ADD: 4,
  CHANGE: 2,
  DELETE: 1,
};

export function redirectUnauthorizedUser(permissions, pagePermissions) {
  permissions.subscribe((value) => {
    let canAccess = pagePermissions.every((el) => value.includes(el));
    if (!canAccess) {
      pop();
    }
  });
}
