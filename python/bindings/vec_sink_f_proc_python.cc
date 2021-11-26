/*
 * Copyright 2021 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(vec_sink_f_proc.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(ac2443596de577249e1f80ae306aca91)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <bokehgui/vec_sink_f_proc.h>
// pydoc.h is automatically generated in the build directory
#include <vec_sink_f_proc_pydoc.h>

void bind_vec_sink_f_proc(py::module& m)
{

    using vec_sink_f_proc    = ::gr::bokehgui::vec_sink_f_proc;


    py::class_<vec_sink_f_proc, gr::bokehgui::base_sink<float>,
        std::shared_ptr<vec_sink_f_proc>>(m, "vec_sink_f_proc", D(vec_sink_f_proc))

        .def(py::init(&vec_sink_f_proc::make),
           py::arg("vlen"),
           py::arg("name"),
           py::arg("nconnections"),
           D(vec_sink_f_proc,make)
        )
        




        
        .def("reset",&vec_sink_f_proc::reset,       
            D(vec_sink_f_proc,reset)
        )

        ;




}








