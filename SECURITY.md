# Security

## Reporting a Vulnerability

Until a private security contact is chosen, report suspected vulnerabilities directly to the project maintainers through a private channel agreed by the group.

Do not open a public issue for:

- exploitable vulnerabilities;
- leaked secrets;
- abuse paths;
- private uploaded media;
- personal information exposed by logs or metadata.

## Secret Handling

Never commit API keys, tokens, credentials, `.env` files, cloud config with secrets, private SSH keys, or service-account files.

If a secret is committed:

1. Treat it as compromised.
2. Revoke or rotate it immediately.
3. Notify maintainers privately.
4. Remove it from history only with maintainer coordination.

## Media Handling

Uploaded or test media can contain personal information. The MVP should minimize retention, avoid public storage of uploads, and document what is stored.

