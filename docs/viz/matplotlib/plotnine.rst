plotnine
========

plotnine implementiert *grammar of graphics* in Python basierend auf `ggplot2
<https://github.com/tidyverse/ggplot2>`_. Die Grammatik erlaubt die einfache
Beschreibung auch von komplexen Grafiken.

Installation
------------

In den meisten Fällen sollte folgende Installation hinreichend sein:

.. code:: console

    $ pipenv install plotnine

Für die Verwendung usammen mit `scikit-learn <https://scikit-learn.org/>`_ und
`scikit-misc <https://github.com/has2k1/scikit-misc>`_ können Extras installiert
werden mit

.. code:: console

    $ pipenv install 'plotnine[all]'
    
Beispiel
--------

#. Importe

   .. code-block:: python

        from plotnine import *
        from plotnine.data import mtcars

#. Streudiagramm

   .. code-block:: python

        (ggplot(mtcars, aes('wt', 'mpg'))
         + geom_point())

   .. figure:: readme-image-1.png
      :alt: plotnine-Streudiagramm

#. Farbliche Unterscheidung der Variablen

   .. code-block:: python

        (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
         + geom_point())

   .. figure:: readme-image-2.png
      :alt: plotnine-Streudiagramm mit farblicher Unterscheidung der Variablen

#. Geglättetes lineares Modell mit Konfidenzintervallen

   .. code-block:: python

        (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
         + geom_point()
         + stat_smooth(method='lm'))

   .. figure:: readme-image-3.png
      :alt: plotnine-Streudiagramm als geglättetes lineares Modell mit
            Konfidenzintervallen

#. Darstellung in separierten Feldern

   .. code-block:: python

        (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
         + geom_point()
         + stat_smooth(method='lm')
         + facet_wrap('~gear'))

   .. figure:: readme-image-4.png
      :alt: plotnine-Streudiagramm als geglättetes lineares Modell mit
            Konfidenzintervallen in separierten Feldern

Interaktive Diagramme
---------------------

Zusammen mit :doc:`/workspace/jupyter/ipywidgets/index` lassen sich auch
interaktive Diagramme erstellen.

#. Importe

   .. code-block:: python

        import matplotlib.pyplot as plt
        import plotnine as p9
        import pandas as pd
        import numpy as np
        from copy import copy
        from ipywidgets import widgets
        from IPython.display import display

        from plotnine.data import mtcars

#. Im folgenden betrachten wir PS auf der x-Achse, Meilen je Gallone auf der
   y-Achse und unterscheiden farblich das Gewicht der Autos:

   .. code-block:: python

        %matplotlib notebook

        p = p9.ggplot(mtcars, p9.aes(x="hp", y="mpg", color="wt")) + \
                p9.geom_point() + p9.theme_linedraw()
        p

   .. figure:: ipython-image-1.png
      :alt: Streugrafik von Autos mit PS, Meilen per Gallone und Gewicht.

#. Nun wählen wir die Autos anhand der Zylinderanzahl aus:

   .. code-block:: python

        # Prepre the list we will use to selec sub-sets of data based on number of cylinders.
        cylList = np.unique( mtcars['cyl'] )

        # The first selection is a drop-down menu for number of cylinders
        cylSelect = widgets.Dropdown(
            options=list(cylList),
            value=cylList[1],
            description='Cylinders:',
            disabled=False,
        )

        # For the widgets to update the same plot, instead of creating one new image every time
        # a selection changes. We keep track of the matplotlib image and axis, so we create only one
        # figure and set of axis, for the first plot, and then just re-use the figure and axis
        # with plotnine's "_draw_using_figure" function.
        fig = None
        axs = None

        # This is the main function that is called to update the plot every time we chage a selection.
        def plotUpdate(*args):

            # Use global variables for matplotlib's figure and axis.
            global fig, axs

            # Get current values of the selection widget
            cylValue = cylSelect.value

            # Create a temporary dataset that is constrained by the user's selections.
            tmpDat = mtcars.loc[(mtcars['cyl'] == cylValue),:]

            # Create plotnine's plot

            # Using the maximum and minimum values we gatehred before, we can keep the plot axis from
            # changing with the cyinder selection
            p = p9.ggplot(tmpDat, p9.aes(x="hp", y="mpg", color="wt")) + \
                p9.geom_point() + p9.theme_linedraw()

            if fig is None:
                # If this is the first time a plot is made in the notebook, we let plotnine create a new
                # matplotlib figure and axis.
                fig, plot = p.draw(return_ggplot=True)
                axs = plot.axs
            else:

                #p = copy(p)
                # This helps keeping old selected data from being visualized after a new selection is made.
                # We delete all previously reated artists from the matplotlib axis.
                for artist in plt.gca().lines +\
                                plt.gca().collections +\
                                plt.gca().artists + plt.gca().patches + plt.gca().texts:
                    artist.remove()

                # If a plot is being updated, we re-use the figure an axis created before.
                p._draw_using_figure(fig, axs)


        cylSelect.observe(plotUpdate, 'value')

        # Display the widgets
        display(cylSelect)

        # Plots the first image, with inintial values.
        plotUpdate()

        # Matplotlib function to make the image fit within the plot dimensions.
        plt.tight_layout()

        # Trick to get the first rendered image to follow the previous "tight_layout" command.
        # without this, only after the first update would the figure be fit inside its dimensions.
        cylSelect.value = cylList[0]

        # The first selection is a drop-down menu for number of cylinders
        cylSelect = widgets.Dropdown(
            options=list(cylList),
            value=cylList[1],
            description='Cylinders:',
            disabled=False,
        )

        # For the widgets to update the same plot, instead of creating one new image every time
        # a selection changes. We keep track of the matplotlib image and axis, so we create only one
        # figure and set of axis, for the first plot, and then just re-use the figure and axis
        # with plotnine's "_draw_using_figure" function.
        fig = None
        axs = None

        # This is the main function that is called to update the plot every time we chage a selection.
        def plotUpdate(*args):

            # Use global variables for matplotlib's figure and axis.
            global fig, axs

            # Get current values of the selection widget
            cylValue = cylSelect.value

            # Create a temporary dataset that is constrained by the user's selections.
            tmpDat = mtcars.loc[(mtcars['cyl'] == cylValue),:]

            # Create plotnine's plot

            # Using the maximum and minimum values we gatehred before, we can keep the plot axis from
            # changing with the cyinder selection
            p = p9.ggplot(tmpDat, p9.aes(x="hp", y="mpg", color="wt")) + \
                p9.geom_point() + p9.theme_linedraw()

            if fig is None:
                # If this is the first time a plot is made in the notebook, we let plotnine create a new
                # matplotlib figure and axis.
                fig, plot = p.draw(return_ggplot=True)
                axs = plot.axs
            else:

                #p = copy(p)
                # This helps keeping old selected data from being visualized after a new selection is made.
                # We delete all previously reated artists from the matplotlib axis.
                for artist in plt.gca().lines +\
                                plt.gca().collections +\
                                plt.gca().artists + plt.gca().patches + plt.gca().texts:
                    artist.remove()

                # If a plot is being updated, we re-use the figure an axis created before.
                p._draw_using_figure(fig, axs)


        cylSelect.observe(plotUpdate, 'value')

        # Display the widgets
        display(cylSelect)

        # Plots the first image, with inintial values.
        plotUpdate()

        # Matplotlib function to make the image fit within the plot dimensions.
        plt.tight_layout()

        # Trick to get the first rendered image to follow the previous "tight_layout" command.
        # without this, only after the first update would the figure be fit inside its dimensions.
        cylSelect.value = cylList[0]

   .. figure:: ipython-image-2.png
      :alt: Streugrafik von Autos mit PS, Meilen per Gallone und Gewicht,
            gefiltert nach Zylinderanzahl.

#. Nun erstellen wir ein Drop-Down-Menü zur Auswahl der Zylinder

   .. code-block:: python

        # We now get the maximum ranges of relevant variables to keep axis constant between images.

        # Get range of weight
        minWt = min(mtcars['wt'])
        maxWt = max(mtcars['wt'])
        # We get all unique values of weigh, sort them, and transform the numpy.array into a python list.
        wtOptions = list( np.sort(np.unique(mtcars.loc[mtcars['cyl']==cylList[0],'wt']))  )

        minHP = min(mtcars['hp'])
        maxHP = max(mtcars['hp'])

        minMPG = min(mtcars['mpg'])
        maxMPG = max(mtcars['mpg'])

        # The first selection is a drop-down menu for number of cylinders
        cylSelect = widgets.Dropdown(
            options=list(cylList),
            value=cylList[1],
            description='Cylinders:',
            disabled=False,
        )

        # For the widgets to update the same plot, instead of creating one new image every time
        # a selection changes. We keep track of the matplotlib image and axis, so we create only one
        # figure and set of axis, for the first plot, and then just re-use the figure and axis
        # with plotnine's "_draw_using_figure" function.
        fig = None
        axs = None

        # This is the main function that is called to update the plot every time we chage a selection.
        def plotUpdate(*args):

            # Use global variables for matplotlib's figure and axis.
            global fig, axs

            # Get current values of the selection widget
            cylValue = cylSelect.value

            # Create a temporary dataset that is constrained by the user's selections.
            tmpDat = mtcars.loc[(mtcars['cyl'] == cylValue),:]

            # Create plotnine's plot

            # Using the maximum and minimum values we gatehred before, we can keep the plot axis from
            # changing with the cyinder selection
            p = p9.ggplot(tmpDat, p9.aes(x="hp", y="mpg", color="wt")) + \
                p9.geom_point() + p9.theme_linedraw() + \
                p9.xlim([minHP, maxHP]) + p9.ylim([minMPG, maxMPG]) + \
                p9.scale_color_continuous(limits=(minWt, maxWt))

            if fig is None:
                fig, plot = p.draw(return_ggplot=True)
                axs = plot.axs
            else:
                #p = copy(p)
                for artist in plt.gca().lines +\
                                plt.gca().collections +\
                                plt.gca().artists + plt.gca().patches + plt.gca().texts:
                    artist.remove()
                p._draw_using_figure(fig, axs)


        cylSelect.observe(plotUpdate, 'value')

        # Display the widgets
        display(cylSelect)

        # Plots the first image, with inintial values.
        plotUpdate()

        # Matplotlib function to make the image fit within the plot dimensions.
        plt.tight_layout()

        # Trick to get the first rendered image to follow the previous "tight_layout" command.
        # without this, only after the first update would the figure be fit inside its dimensions.
        cylSelect.value = cylList[0]

   .. figure:: ipython-image-3.png
      :alt: Streugrafik von Autos mit PS, Meilen per Gallone und Gewicht,
            mit Drop-Down-Menü zur Auswahl der Zylinderanzahl.

#. Nun schränken wir mit einem Bereichsregler die Daten basierend auf dem
   Fahrzeuggewicht ein:

   .. code-block:: python

        # The first selection is a drop-down menu for number of cylinders
        cylSelect = widgets.Dropdown(
            options=list(cylList),
            value=cylList[1],
            description='Cylinders:',
            disabled=False,
        )

        # The second selection is a range of weights
        wtSelect = widgets.SelectionRangeSlider(
            options=wtOptions,
            index=(0,len(wtOptions)-1),
            description='Weight',
            disabled=False
        )

        widgetsCtl = widgets.HBox([cylSelect, wtSelect])

        # The range of weights needs to always be dependent on the cylinder selection.
        def updateRange(*args):
            '''Updates the selection range from the slider depending on the cylinder selection.'''
            cylValue = cylSelect.value

            wtOptions = list( np.sort(np.unique(mtcars.loc[mtcars['cyl']==cylValue,'wt']))  )

            wtSelect.options = wtOptions
            wtSelect.index = (0,len(wtOptions)-1)

        cylSelect.observe(updateRange,'value')

        # For the widgets to update the same plot, instead of creating one new image every time
        # a selection changes. We keep track of the matplotlib image and axis, so we create only one
        # figure and set of axis, for the first plot, and then just re-use the figure and axis
        # with plotnine's "_draw_using_figure" function.
        fig = None
        axs = None

        # This is the main function that is called to update the plot every time we chage a selection.
        def plotUpdate(*args):

            # Use global variables for matplotlib's figure and axis.
            global fig, axs

            # Get current values of the selection widgets
            cylValue = cylSelect.value
            wrRange = wtSelect.value

            # Create a temporary dataset that is constrained by the user's selections.
            tmpDat = mtcars.loc[(mtcars['cyl'] == cylValue) & \
                                (mtcars['wt'] >= wrRange[0]) & \
                                (mtcars['wt'] <= wrRange[1]),:]

            # Create plotnine's plot

            p = p9.ggplot(tmpDat, p9.aes(x="hp", y="mpg", color="wt")) + \
                p9.geom_point() + p9.theme_linedraw() + \
                p9.xlim([minHP, maxHP]) + p9.ylim([minMPG, maxMPG]) + \
                p9.scale_color_continuous(limits=(minWt, maxWt))

            if fig is None:
                fig, plot = p.draw(return_ggplot=True)
                axs = plot.axs
            else:

                for artist in plt.gca().lines +\
                                plt.gca().collections +\
                                plt.gca().artists + plt.gca().patches + plt.gca().texts:
                    artist.remove()
                p._draw_using_figure(fig, axs)


        cylSelect.observe(plotUpdate, 'value')
        wtSelect.observe(plotUpdate, 'value')

        # Display the widgets
        display(widgetsCtl)

        # Plots the first image, with inintial values.
        plotUpdate()

        # Matplotlib function to make the image fit within the plot dimensions.
        plt.tight_layout()

        # Trick to get the first rendered image to follow the previous "tight_layout" command.
        # without this, only after the first update would the figure be fit inside its dimensions.
        cylSelect.value = cylList[0]

    .. figure:: ipython-image-4.png
       :alt: Streugrafik von Autos mit PS, Meilen per Gallone und Gewicht,
             mit Bereichsregler für das Fahrzeuggewicht.

#. Schließlich ändern wir noch einige Diagrammeigenschaften, um eine
   verständlicherw Abbildung zu erhalten:

   .. code-block:: python

        # The first selection is a drop-down menu for number of cylinders
        cylSelect = widgets.Dropdown(
            options=list(cylList),
            value=cylList[1],
            description='Cylinders:',
            disabled=False,
        )

        # The second selection is a range of weights
        wtSelect = widgets.SelectionRangeSlider(
            options=wtOptions,
            index=(0,len(wtOptions)-1),
            description='Weight',
            disabled=False
        )

        widgetsCtl = widgets.HBox([cylSelect, wtSelect])

        # The range of weights needs to always be dependent on the cylinder selection.
        def updateRange(*args):
            '''Updates the selection range from the slider depending on the cylinder selection.'''
            cylValue = cylSelect.value

            wtOptions = list( np.sort(np.unique(mtcars.loc[mtcars['cyl']==cylValue,'wt']))  )

            wtSelect.options = wtOptions
            wtSelect.index = (0,len(wtOptions)-1)

        cylSelect.observe(updateRange,'value')

        fig = None
        axs = None

        # This is the main function that is called to update the plot every time we chage a selection.
        def plotUpdate(*args):

            # Use global variables for matplotlib's figure and axis.
            global fig, axs

            # Get current values of the selection widgets
            cylValue = cylSelect.value
            wrRange = wtSelect.value

            # Create a temporary dataset that is constrained by the user's selections of
            # number of cylinders and weight.
            tmpDat = mtcars.loc[(mtcars['cyl'] == cylValue) & \
                                (mtcars['wt'] >= wrRange[0]) & \
                                (mtcars['wt'] <= wrRange[1]),:]

            # Create plotnine's plot showing all data ins smaller grey points, and
            # the selected data with coloured points.
            p = p9.ggplot(tmpDat, p9.aes(x="hp", y="mpg", color="wt") ) + \
                p9.geom_point(mtcars, p9.aes(x="hp", y="mpg"), color="grey") + \
                p9.geom_point(size=3) + p9.theme_linedraw() + \
                p9.xlim([minHP, maxHP]) + p9.ylim([minMPG, maxMPG]) + \
                p9.scale_color_continuous(name="spring",limits=(np.floor(minWt), np.ceil(maxWt))) +\
                p9.labs(x = "Horse-Power", y="Miles Per Gallon", color="Weight" )

            if fig is None:
                fig, plot = p.draw(return_ggplot=True)
                axs = plot.axs
            else:

                for artist in plt.gca().lines +\
                                plt.gca().collections +\
                                plt.gca().artists + plt.gca().patches + plt.gca().texts:
                    artist.remove()
                p._draw_using_figure(fig, axs)


        cylSelect.observe(plotUpdate, 'value')
        wtSelect.observe(plotUpdate, 'value')

        # Display the widgets
        display(widgetsCtl)

        # Plots the first image, with inintial values.
        plotUpdate()

        # Matplotlib function to make the image fit within the plot dimensions.
        plt.tight_layout()

        # Trick to get the first rendered image to follow the previous "tight_layout" command.
        # without this, only after the first update would the figure be fit inside its dimensions.
        cylSelect.value = cylList[0]

    .. figure:: ipython-image-5.png
       :alt: Streugrafik von Autos mit PS, Meilen per Gallone und Gewicht
             mit optimierter Darstellung.

Zum Weiterlesen
---------------

.. seealso::

   `plotnine documentation <https://plotnine.readthedocs.io/>`_
        API-Referenz, Gallerie, Tutorials etc.
   `ggplot2 documentation <http://ggplot2.tidyverse.org/reference/index.html>`_
        plotnine verwendet eine ähnliche API und Pipeline wie ggplt2
   `Grammer of graphics with plotnine <https://www.kaggle.com/residentmario/grammer-of-graphics-with-plotnine-optional/>`_
        Gutes Tutorial zur Einführung in plotnine als Teil eines
        `Datenvisualisierung-Track <https://www.kaggle.com/learn/data-visualization>`_ von kaggle.
   `Paul Teehan: Plotnine is the best Python implementation of R's ggplot2 <https://web.archive.org/web/20181012022314/http://pltn.ca/plotnine-superior-python-ggplot/>`_
        Vergleich zwischen plotnine und ggplot2, v.a. in Bezug auf die API-Kompatibilität.
   `Python Plotting for Exploratory Analysis <https://pythonplot.com/>`_
        Eine Liste von Plots für die explorative Datenanalyse und wie sie mit
        verschiedenen Bibliotheken erstellt werden können.
   `Introduction to Plotnine <http://www.mbel.io/2019/08/06/introduction-to-plotnine-ggplot-port-in-python/>`_
        Erläutert die Hauptaspekte von plotnine und zeigt, wie die Bibliothek
        verwendet werden kann.
   `Making Plots With plotnine <https://datacarpentry.org/python-ecology-lesson/07-visualization-ggplot-python/index.html>`_
        Eine Einführung in `The Grammar of Graphics
        <https://www.springer.com/gp/book/9780387245447>`_ und die Verwendung
        von plotnine. Dies ist Teil des Kurses von`Data Carpentry `Data Analysis
        and Visualization in Python for Ecologists
        <https://datacarpentry.org/python-ecology-lesson/>`_.

