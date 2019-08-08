===============================
Deployment und Release Branches
===============================

Deployment-Branches
===================

Sie empfehlen sich, wenn ihr z.B. den Release-Zeitpunkt nicht
selbst bestimmen könnt, beispielsweise wenn eine iOS-Anwendung die
App-Store-Validierung bestehen muss oder euch nur ein festes Zeitfenster für
die Bereitstellung zur Verfügung steht. In diesem Fall empfiehlt sich ein
Production-Branch ``prod``, der den bereitgestellten Code widerspiegelt. Ein
solcher Arbeitsablauf verhindert den zusätzlichen Arbeitsaufwand bei ``git
flow`` beim Releasing, Tagging und Merging.

Angenommen, ihr verfügt über eine ``test``-, ``stage``- und ``prod``-Umgebung,
dann wird zunächst ein *Merge Request* für den ``test``-Branch gestellt. Wenn
die Tests bestanden werden, können die Änderungen auch in den ``stage``-Branch
übernommen werden. Wenn die QA beschließt, dass der Code produktionsreif ist,
kann er in den ``master``-Branch übernommen werden. Dieser Vorgang kann sich
mehrfach wiederholen, bis z.B. der Zeitpunkt für das *Going Life* dieser
Änderungen gekommen ist und ein ``prod``-Branch erstellt werden kann.

Release-Branches
================

Wenn Software an Kunden geliefert werden soll, empfehlen sich Release-Branches.
In diesem Fall sollte jeder Branch eine *Minor Version*, also z.B. ``2.7`` oder
``3.4`` enthalten. Üblicherweise werden diese Branches so spät wie möglich aus
dem ``master``-Branch erzeugt. Dadurch wird bei Bugfixes die Anzahl der Merges,
die auf mehrere Branches verteilt werden müssen, reduziert. Nachdem ein neuer
Release-Branch erstellt wurde, erhält dieser nur noch Bugfixes. Meist werden
diese zunächst in den ``master`` übernommen und anschließend von dort mit
`git cherry-pick <https://git-scm.com/docs/git-cherry-pick>`_ in den
Release-Branch übernommen. Dieser *upstream first*-Ansatz wird z.B. von `Google
<https://www.chromium.org/chromium-os/chromiumos-design-docs/upstream-first>`_
und `Red Hat
<https://www.redhat.com/en/blog/a-community-for-using-openstack-with-red-hat-rdo>`_
verwendet. Jedes Mal, wenn ein Bugfix in einen Release-Branch übernommen wurde,
wird das Release mit einem `Tag
<https://git-scm.com/book/de/v1/Git-Grundlagen-Tags>`_ um eine Patch-Version
angehoben, s.a. `Semantic Versioning <https://semver.org/>`_.
