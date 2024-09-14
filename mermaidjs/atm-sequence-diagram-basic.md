Mermaid JS experimentation with the chart described https://www.youtube.com/watch?v=pCK6prSq8aw&t=31s

try these extensions
https://github.com/bpruitt-goddard/vscode-mermaid-syntax-highlight

look at this formatting post
https://notepad.onghu.com/2024/making-mermaid-sequence-diagrams-prettier-part1/

docs https://mermaid.js.org/syntax/sequenceDiagram.html

cheat sheet https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/

```mermaid

---
title: A simple diagram
config:
  showSequenceNumbers: false
---

sequenceDiagram
%% this is a comment

    actor customer
    participant ATM as ATM
    participant server as Bank Server
    participant account as Account

    customer->>ATM:insert Card

    activate ATM

    ATM->>server:Verify Card

activate server

    alt If card is valid
        server-->>ATM:Card OK
        ATM->>customer:Request PIN
    else
        server-->>ATM: Card Invalid
        ATM->>customer:Eject Card
    end

    customer->>ATM:enter PIN
    ATM->>server:Verify PIN

Note right of customer: Text in note

    alt If PIN is valid
        server-->>ATM:PIN OK
        ATM->>customer:Request Amount to Withdraw
    else
        server-->>ATM: PIN Invalid
        ATM->>customer:Eject Card
    end

    customer-->>ATM:enter Amount
    ATM->>server: start Transaction
    server->>account: sufficient Funds?

Note over ATM,account: This note spans lots of boxes

activate account

    alt If funds are sufficient

        account-->>server: Funds OK
        server->>account:Withdraw Funds
        account-->>server:Withdraw OK
        server-->>ATM: Transaction OK
        ATM->>customer: Dispense cash
    else
        account-->>server: Insufficient Funds

        server-->>ATM: Transaction Failed
    end
    deactivate ATM

    deactivate account
    deactivate server

    ATM->>customer:Eject Card

```
