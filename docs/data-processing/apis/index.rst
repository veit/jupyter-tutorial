**A**\pplication **P**\rogramming **I**\nterface (API)
======================================================

APIs can be used to provide the data. :doc:`fastapi/index` is a library that can
generate APIs and documentation based on `OpenAPI <https://www.openapis.org/>`_
and `JSON Schema <http://json-schema.org/>`_. :doc:`grpc/index`, on the other
hand, is a modern open source RPC framework that uses HTTP/2 and QUIC.

To determine the design of your API, you can follow `Zalando’s API Styleguide
<https://opensource.zalando.com/restful-api-guidelines/>`_. Later, you can use
`Zally <https://github.com/zalando/zally>`_ to automatically check the quality
of your API. You can also define your own rules for Zally, see `Rule Development
Manual
<https://github.com/zalando/zally/blob/master/documentation/rule-development.md>`_.

.. seealso::
   * `REST API Design – Resource Modeling
     <https://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling>`_
   * `Richardson Maturity Model – steps toward the glory of REST
     <https://martinfowler.com/articles/richardsonMaturityModel.html>`_
   * `Irresistible APIs – Designing web APIs that developers will love
     <https://www.manning.com/books/irresistible-apis>`_
   * `REST in Practice
     <https://www.oreilly.com/library/view/rest-in-practice/9781449383312/>`_
   * `Build APIs You Won’t Hate <https://leanpub.com/build-apis-you-wont-hate>`_
   * `Representational State Transfer (REST)
     <https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    fastapi/index
    grpc/index
